from flask import Flask, request, jsonify
import os
import requests
from datetime import datetime

app = Flask(__name__)

def enviar_telegram(mensagem):
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")

    if token and chat_id:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": mensagem,
            "parse_mode": "Markdown"
        }
        requests.post(url, data=payload)

@app.route("/leao-ia", methods=["POST"])
def receber_alerta():
    try:
        dados = request.get_json()
        mensagem = dados.get("message", "⚠️ Mensagem vazia")

        # Registro do horário do servidor
        agora = datetime.now().strftime("%d/%m | %H:%M")
        mensagem_final = f"{mensagem}\n📅 {agora}"

        enviar_telegram(mensagem_final)

        return jsonify({"status": "Mensagem recebida e enviada ao Telegram."}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
