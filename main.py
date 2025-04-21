from flask import Flask, request
import requests
from utils.sentimento import analisar_sentimento
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
    ativo = data.get("ticker", "Desconhecido").upper()
    timeframe = data.get("interval", "Desconhecido")
    preco = data.get("close", "N/A")

    sentimento = analisar_sentimento()
    agora_data = datetime.now().strftime("📅 %d/%m")
    agora_hora = datetime.now().strftime("⏰ %H:%M")

    if "COMPRA" in mensagem.upper():
        direcao = "🟢 *COMPRA*"
    elif "VENDA" in mensagem.upper():
        direcao = "🔴 *VENDA*"
    else:
        direcao = "⚪ SINAL DESCONHECIDO"

    tendencia = "📊 Tendência do ativo: A favor da tendência" if "A FAVOR" in mensagem.upper() else "📊 Tendência do ativo: ⚠️ Contra a tendência"
    tendencia_btc = "Alta" if "A FAVOR" in mensagem.upper() else "Baixa"

    mensagem_final = f"""
📡 *LEÃO IA* 🦁 - Alerta Detectado
{direcao}   |   *{ativo}*
{tendencia}  
🧠 Sentimento: {sentimento}  
⏱️ Time Frame: {timeframe}  
📈 Preço: {preco}  
📊 Tendência do BTC: {tendencia_btc}  
{agora_data} | {agora_hora}
"""

    send_telegram_message(mensagem_final.strip())
    return {"status": "Mensagem enviada com sucesso"}, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
