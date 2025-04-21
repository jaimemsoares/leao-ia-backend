import requests

def analisar_sentimento(texto=None):
    try:
        response = requests.get("https://open-api.coinglass.com/api/pro/v1/fgi/index")
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
            return "⚠️ Erro Coinglass"
    except Exception as e:
        return f"⚠️ Erro Sentimento: {str(e)}"
