import requests

ELEVENLABS_URL = "https://api.elevenlabs.io/v1/text-to-speech"
ELEVENLABS_API_KEY = ""

def texto_a_voz(texto):
    url = ELEVENLABS_URL
    headers = {"xi-api-key": ELEVENLABS_API_KEY}
    data = {"text": texto, "voice": "Bella"}  # Puedes cambiar la voz
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        with open("audio.mp3", "wb") as f:
            f.write(response.content)
        return "audio.mp3"
    else:
        return None