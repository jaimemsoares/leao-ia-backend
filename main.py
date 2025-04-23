from flask import Flask, request, jsonify
from utils.sentimento import analisar_sentimento
from utils.tendencia import analisar_tendencia_btc
from datetime import datetime
import pytz
import os

app = Flask(__name__)

@app.route('/leao-ia', methods=['POST'])
def receber_alerta():
    try:
        if request.is_json:
            dados = request.get_json()
        else:
            # Se não for JSON, tenta tratar como texto simples
            dados = {
                "message": request.data.decode('utf-8')
            }

        print("🔔 Alerta recebido:", dados)
        # Aqui você pode adicionar envio ao Telegram se quiser testar

        return jsonify({"status": "ok", "dados_recebidos": dados}), 200

    except Exception as e:
        print("⚠️ Erro ao processar alerta:", str(e))
        return jsonify({"status": "erro", "mensagem": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
