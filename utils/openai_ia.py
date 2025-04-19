import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def analisar_texto_com_openai(texto):
    prompt = f"""
    Analise o seguinte texto do ponto de vista do sentimento e impacto econômico:
    
    "{texto}"
    
    Responda no formato:
    - Sentimento: (Positivo, Neutro, Negativo)
    - Impacto Econômico: (Alto, Moderado, Estável)
    """
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )
    conteudo = resposta.choices[0].message.content.strip()
    return conteudo
