from flask import Flask, request, jsonify
from utils.sentimento import analisar_sentimento
from utils.tendencia import analisar_tendencia_btc
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/leao-ia", methods=["POST"])
def receber_alerta():
    data = request.json
    ticker = data.get("ticker", "Ativo Desconhecido")
    preco = data.get("close", "N/A")
    intervalo = data.get("interval", "Período desconhecido")
    direcao = "🟢 COMPRA" if "COMPRA" in data.get("message", "") else "🔴 VENDA"

    sentimento = analisar_sentimento()
    tendencia_btc = analisar_tendencia_btc()

    # Horário formatado
    fuso = pytz.timezone("America/Sao_Paulo")
    agora = datetime.now(fuso)
    hora = agora.strftime("%H:%M")
    data_br = agora.strftime("%d/%m")

    mensagem_final = f"""
📡 *LEÃO IA* 🦁 - Alerta Detectado
{direcao}   |   *{ticker}*
📊 Tendência do ativo: {tendencia_btc['ativo']}
🧠 Sentimento: {sentimento}
⏱️ Time Frame: {intervalo}
📈 Preço: {preco}
📊 Tendência Exclusiva do BTC: {tendencia_btc['btc']}
📅 {data_br} | ⏰ {hora}
"""

    print("Mensagem para Telegram:")
    print(mensagem_final)

    return jsonify({"status": "ok", "mensagem_enviada": mensagem_final})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
