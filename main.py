from flask import Flask, request
import requests
from utils.openai_ia import analisar_texto_com_openai

from datetime import datetime
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")


def send_telegram_message(mensagem):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": mensagem,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)


@app.route('/leao-ia', methods=['POST'])
def webhook():
    try:
        data = request.get_json(force=True)
    except:
        data = request.data.decode('utf-8')
        data = {"message": data}

    mensagem = data.get("message", "")
    ativo = data.get("ticker", "Ativo Desconhecido")
    timeframe = data.get("interval", "Período desconhecido")
    preco = data.get("close", "N/A")

    texto_externo = "Mercado otimista com crescimento apesar da inflação"
    ia_resposta = analisar_texto_com_openai(texto_externo)

    agora = datetime.now().strftime("%d/%m %H:%M")

    direcao = "🟢 *COMPRA*" if "COMPRA" in mensagem.upper() else "🔴 *VENDA*"

    mensagem_final = f"""
📡 *LEÃO IA* - Alerta Detectado
{direcao} detectada em *{ativo}* ({timeframe})
📈 *Preço*: {preco}
🧠 *Sentimento*: {ia_resposta}
🌎 *Impacto Econômico*: {ia_resposta}
⏰ *Horário*: {agora}
"""

    send_telegram_message(mensagem_final.strip())
    return {"status": "Mensagem enviada com sucesso"}, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
