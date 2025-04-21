import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

client = openai.OpenAI()

def analisar_sentimento(texto):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um analista de sentimento de mercado financeiro. Classifique o texto como Positivo 😃, Negativo 😞 ou Neutro 😐."},
                {"role": "user", "content": texto}
            ]
        )
        resultado = response.choices[0].message.content.strip()
        return resultado
    except Exception as e:
        return f"⚠️ Erro IA: {str(e)}"
