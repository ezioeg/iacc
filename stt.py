import openai

OPENAI_API_KEY = ""
openai.api_key = OPENAI_API_KEY

def voz_a_texto(archivo_audio):
    with open(archivo_audio, "rb") as audio_file:
        transcripcion = openai.Audio.transcribe("whisper-1", audio_file)
    return transcripcion["text"]