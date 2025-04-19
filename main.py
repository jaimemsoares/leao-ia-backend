
from flask import Flask, request
import requests
from utils.sentimento import analisar_sentimento, avaliar_impacto_economico
from datetime import datetime

app = Flask(__name__)

BOT_TOKEN = "7729732058:AAGmtgMI2LEso_ifOxEb4__I2rcM_Dr6Dwk"
CHAT_ID = "-1002466281231"

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
    data = request.json
    ativo = data.get("ticker", "Ativo Desconhecido")
    timeframe = data.get("interval", "Período desconhecido")
    preco = data.get("close", "N/A")
    texto_externo = "Mercado otimista com crescimento apesar da inflação"
    sentimento = analisar_sentimento(texto_externo)
    economia = avaliar_impacto_economico(texto_externo)
    agora = datetime.now().strftime("%d/%m %H:%M")
    direcao = "🟢 *COMPRA*" if "COMPRA" in data.get("message", "").upper() else "🔴 *VENDA*"
    mensagem_final = f"""📡 *LEÃO IA* - Alerta Detectado
{direcao} detectada em *{ativo}* ({timeframe})
📈 *Preço*: {preco}
🧠 *Sentimento*: {sentimento}
🌎 *Impacto Econômico*: {economia}
⏰ *Horário*: {agora}"""
    send_telegram_message(mensagem_final.strip())
   
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    
     return {"status": "Mensagem enviada com sucesso"}, 200

