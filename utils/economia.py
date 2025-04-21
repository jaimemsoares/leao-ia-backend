
def avaliar_impacto_economico(texto):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um analista de impacto econômico. Classifique o texto como 🚨 Alto Impacto, ⚠️ Impacto Moderado ou 🌐 Estável."},
                {"role": "user", "content": texto}
            ]
        )
        resultado = response.choices[0].message.content.strip()
        return resultado
    except Exception as e:
        return f"⚠️ Erro IA: {str(e)}"
