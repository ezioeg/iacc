from twilio.rest import Client

TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""
TWILIO_PHONE_NUMBER = ""
CLIENT_PHONE_NUMBER = ""

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def hacer_llamada(numero_cliente, url_audio):
    llamada = client.calls.create(
        to=numero_cliente,
        from_=TWILIO_PHONE_NUMBER,
        url=url_audio  # Aquí debe ir un archivo XML de Twilio con el audio
    )
    return llamada.sid