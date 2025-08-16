import requests

# --- Configuración de Telegram ---
TELEGRAM_BOT_TOKEN = "7958057711:AAH5wcldVXlF4PcOiqdQK6ikZaJquMFT3v0"
TELEGRAM_CHAT_ID = "857300743"
TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

def send_telegram_message(message):
    """Envía un mensaje de texto a un chat de Telegram."""
    try:
        payload = {
            'chat_id': TELEGRAM_CHAT_ID,
            'text': message,
            'parse_mode': 'Markdown'
        }
        response = requests.post(TELEGRAM_API, data=payload)
        response.raise_for_status()  # Lanza una excepción si la solicitud falla
        print("✅ Mensaje de Telegram enviado con éxito.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al enviar el mensaje de Telegram: {e}")

# --- Envía el mensaje de prueba ---
test_message = "✅ Mensaje de prueba desde Python. ¡El bot está funcionando correctamente!"
send_telegram_message(test_message)