#!/bin/bash

# --- Configuración Principal ---
USER="" # Usuario de MySQL
PASSWORD="" # Contraseña de MySQL
BACKUP_DIR="" # Directorio donde se guardarán los respaldos temporales
REPO_DIR="" # Directorio del repositorio Git en el servidor
GIT_REPO="" # URL del repositorio Git
SERVER_NAME="" # Nombre del servidor (opcional, para notificaciones)

# --- Configuración Telegram ---
TELEGRAM_BOT_TOKEN="" # Token del bot de Telegram
TELEGRAM_CHAT_ID="" # ID del chat de Telegram
TELEGRAM_API="https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage"

# --- Variables de estado ---
BACKUP_STATUS=0
ERROR_LOG=""
SUCCESSFUL_DBS=""

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
        BACKUP_STATUS=1
        ERROR_LOG+="• \`$DB\`"$'\n'
    else
        SUCCESSFUL_DBS+="• \`$DB\`"$'\n'
    fi
done

# --- Subir a Git ---
cd $REPO_DIR

# Configurar Git solo para este repositorio
git config --local user.name "" # Nombre de usuario de Git
git config --local user.email "" # Email de usuario de Git

# Inicializar repo (solo primera vez)
if [ ! -d ".git" ]; then
    git clone $GIT_REPO .
fi

# Sincronizar cambios remotos primero
git pull origin main

# Copiar nuevos respaldos (sobrescribiendo los existentes)
cp -f $BACKUP_DIR/*.sql .

FILES_LIST=""
for f in "$BACKUP_DIR"/*.sql; do
    [ -e "$f" ] || continue
    base=$(basename "$f")
    FILES_LIST+="• \`$base\`"$'\n'
done


# Commit y push
git add .
git commit -m "Backup automático de bases de datos ($(date '+%d/%m/%Y %H:%M'))"
git push origin main
PUSH_STATUS=$?

# --- Notificación por Telegram (unificada) ---
MESSAGE=""
if [ $BACKUP_STATUS -eq 0 ] && [ $PUSH_STATUS -eq 0 ]; then
    # Éxito total
    MESSAGE="✅ *Respaldo exitoso*
    *Servidor*: $SERVER_NAME
    *Fecha*: $(date '+%d/%m/%Y %H:%M')
    *Bases de datos respaldadas*:
	${SUCCESSFUL_DBS}
    *Archivos subidos a GitHub*:
	${FILES_LIST}"
elif [ $BACKUP_STATUS -ne 0 ]; then
    # Fallo en el respaldo de al menos una BD
    MESSAGE="⚠️ *Fallo parcial en el respaldo*
    *Servidor*: $SERVER_NAME
    *Fecha*: $(date '+%d/%m/%Y %H:%M')
    *Bases de datos con error*:
	${ERROR_LOG}
    *Bases de datos exitosas*:
	${SUCCESSFUL_DBS}
    *Estado de Git*: ${PUSH_STATUS}"
elif [ $PUSH_STATUS -ne 0 ]; then
    # Fallo en el push a Git
    MESSAGE="❌ *Fallo en la subida a GitHub*
    *Servidor*: $SERVER_NAME
    *Fecha*: $(date '+%d/%m/%Y %H:%M')
    *Bases de datos respaldadas*:
	${SUCCESSFUL_DBS}
    *Error*: No se pudo subir los archivos. Por favor, revisa manualmente."
fi

# Enviar la notificación consolidada
if [ -n "$MESSAGE" ]; then
    curl -s -X POST $TELEGRAM_API \
        -d chat_id=$TELEGRAM_CHAT_ID \
        -d text="$MESSAGE" \
        -d parse_mode="Markdown" > /dev/null
fi
