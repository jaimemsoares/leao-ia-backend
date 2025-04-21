import requests
import os

def analisar_sentimento(texto=None):
    try:
        url = "https://open-api.coinglass.com/api/pro/v1/fgi/index"
        headers = {
            "accept": "application/json",
        }

        # Verifica se existe uma chave Coinglass configurada
        coinglass_key = os.environ.get("COINGLASS_API_KEY")
        if coinglass_key:
            headers["coinglassSecret"] = coinglass_key  # chave via header

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            fgi = response.json().get("data", {})
            valor = fgi.get("now", 50)
            if valor >= 70:
                return "😃 Positivo para compra"
            elif valor <= 30:
                return "😡 Positivo para venda"
            else:
                return "😐 Neutro"
        else:
            return f"⚠️ Erro Coinglass ({response.status_code})"
    except Exception as e:
        return f"⚠️ Erro Sentimento: {str(e)}"
