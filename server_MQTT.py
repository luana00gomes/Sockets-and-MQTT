import mosquitto

BROKER_ADDRESS = 'localhost'  # Endereço IP do broker
PORT = 1883  # Porta para se conectar ao broker

broker = mosquitto.Mosquitto()
broker.bind(BROKER_ADDRESS, PORT)

broker.username_pw_set('usuario', 'senha')

broker.loop_forever()