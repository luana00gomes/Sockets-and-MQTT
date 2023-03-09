import socket
import time
# Define o endereço do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 8080        # Porta que o servidor estará escutando

# Cria um objeto socket
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Conecta ao servidor
        s.connect((HOST, PORT))

        # Envia uma mensagem ao servidor
        s.sendall(b'Ola, servidor! Quanta memoria esta em uso?')

        # Recebe a resposta do servidor
        data = s.recv(1024)
    # Imprime a resposta do servidor
    print('Resposta do servidor:', repr(data))
    time.sleep(2)


