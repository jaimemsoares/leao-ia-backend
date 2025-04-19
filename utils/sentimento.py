
def analisar_sentimento(texto):
    texto = texto.lower()
    positivo = ["alta", "otimista", "bullish", "subida", "crescimento"]
    negativo = ["queda", "pessimista", "bearish", "despencar", "crise"]
    score = 0
    for palavra in positivo:
        if palavra in texto:
            score += 1
    for palavra in negativo:
        if palavra in texto:
            score -= 1
    if score > 0:
        return "😃 Positivo"
    elif score < 0:
        return "😞 Negativo"
    else:
        return "😐 Neutro"

def avaliar_impacto_economico(texto):
    texto = texto.lower()
    alto_impacto = ["fed", "juros", "cpi", "inflação", "recessão"]
    moderado_impacto = ["balanço", "gdp", "emprego"]
    impacto = "🌐 Estável"
    for palavra in alto_impacto:
        if palavra in texto:
            impacto = "🚨 Alto Impacto"
            break
    if impacto == "🌐 Estável":
        for palavra in moderado_impacto:
            if palavra in texto:
                impacto = "⚠️ Impacto Moderado"
                break
    return impacto
