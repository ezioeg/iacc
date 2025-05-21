def analizar_texto(texto_usuario):
    respuesta = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "Eres un operador de call center."},
                  {"role": "user", "content": texto_usuario}]
    )
    return respuesta["choices"][0]["message"]["content"]