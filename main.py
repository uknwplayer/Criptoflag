
import os
import requests

# Acessando os secrets
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(url, json=payload)
    return response.json()

def main():
    # Enviar uma mensagem de teste
    response = send_telegram_message("Esta é uma mensagem de teste!")
    print(response)

if __name__ == "__main__":
    main()
