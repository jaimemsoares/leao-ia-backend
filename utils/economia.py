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
