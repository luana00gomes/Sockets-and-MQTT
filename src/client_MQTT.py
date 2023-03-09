import paho.mqtt.client as mqtt
import psutil
import time

BROKER_ADDRESS = 'localhost'  # Endereço IP do broker
PORT = 8080
TOPIC = 'memoria'  # Tópico para publicar e subscrever o uso de memória

client = mqtt.Client()

# Definição da função callback que será chamada quando receber uma mensagem no tópico configurado
def on_message(client, userdata, message):
    # Converte a mensagem recebida em string
    mem_percent = str(message.payload.decode("utf-8"))
    print("Uso de memória recebido: ", mem_percent)

# Configura o cliente para chamar a função callback quando receber uma mensagem no tópico configurado
client.on_message = on_message

client.connect(BROKER_ADDRESS, PORT)
client.subscribe(TOPIC)

while True:
    # Obtem o uso de memória do computador
    mem_percent = psutil.virtual_memory().percent
    # Publica o uso de memória no tópico
    client.publish(TOPIC, mem_percent)
    # Aguarda mensagens recebidas por 5 segundos
    client.loop(timeout=5.0)
