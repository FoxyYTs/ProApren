backup_db.sh



#!/bin/bash



# --- Configuración Principal ---

USER="root" # Usuario de MariaDB

PASSWORD="<password>" # Contraseña (vacía por defecto en XAMPP)

BACKUP_DIR="/opt/lampp/backups/db" # Carpeta para respaldos

REPO_DIR="/opt/lampp/backups/repo" # Carpeta del repositorio git

GIT_REPO="<url>" # URL del repo



# --- Configuración Telegram ---

TELEGRAM_BOT_TOKEN="<token>" # Token del bot de Telegram

TELEGRAM_CHAT_ID="><chat_id>" # ID del chat o canal de Telegram

TELEGRAM_API="https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage"



# --- Obtener lista de todas las bases de datos ---

DATABASES=$(/opt/lampp/bin/mysql -u $USER -p$PASSWORD -e "SHOW DATABASES;" | grep -Ev "(Database|information_schema|performance_schema|mysql|phpmyadmin)")



# --- Crear directorios si no existen ---

mkdir -p $BACKUP_DIR

mkdir -p $REPO_DIR



# --- Respaldo cada base de datos ---

for DB in $DATABASES; do

    BACKUP_FILE="$BACKUP_DIR/${DB}.sql"

    /opt/lampp/bin/mysqldump -u $USER -p$PASSWORD $DB > $BACKUP_FILE

    if [ $? -ne 0 ]; then

        ERROR_MESSAGE="❌ Falló el respaldo de $DB"

        curl -s -X POST $TELEGRAM_API \

            -d chat_id=$TELEGRAM_CHAT_ID \

            -d text="$ERROR_MESSAGE" \

            -d parse_mode="Markdown" > /dev/null

        continue

    fi

done



# --- Subir a Git ---

cd $REPO_DIR



# Configurar Git solo para este repositorio

git config --local user.name "FoxyYTs"

git config --local user.email "foxy200442@gmail.com"



# Inicializar repo (solo primera vez)

if [ ! -d ".git" ]; then

    git clone $GIT_REPO .

fi



# Sincronizar cambios remotos primero

git pull origin main



# Copiar nuevos respaldos (sobrescribiendo los existentes)

cp -f $BACKUP_DIR/*.sql .



# Commit y push

git add .

git commit -m "Backup automático de bases de datos ($(date '+%d/%m/%Y %H:%M'))"

git push origin main

PUSH_STATUS=$?



# --- Notificación por Telegram ---

if [ $PUSH_STATUS -eq 0 ]; then

    DB_LIST=$(echo $DATABASES | tr '\n' ' ')

    MESSAGE="✅ Respaldo exitoso

📅 Fecha: $(date '+%d/%m/%Y %H:%M')

🗄 Bases de datos: \`$DB_LIST\`

💾 Archivos: $(ls $BACKUP_DIR/*.sql | xargs -n 1 basename | tr '\n' ' ')

🔄 Control de versiones: GitHub"

    curl -s -X POST $TELEGRAM_API \

        -d chat_id=$TELEGRAM_CHAT_ID \

        -d text="$MESSAGE" \

        -d parse_mode="Markdown" > /dev/null

else

    MESSAGE="❌ Falló el respaldo

📅 Fecha: $(date '+%d/%m/%Y %H:%M')

⚠️ Error al subir los respaldos a GitHub

🔍 Verifica los logs del servidor"

    curl -s -X POST $TELEGRAM_API \

        -d chat_id=$TELEGRAM_CHAT_ID \

        -d text="$MESSAGE" \

        -d parse_mode="HTML" > /dev/null

fi