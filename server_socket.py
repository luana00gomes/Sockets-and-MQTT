import socket

# Define o endereço do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 8080        # Porta que o servidor estará escutando

# Cria um objeto socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Vincula o socket ao endereço e porta especificados
    s.bind((HOST, PORT))

    # Aguarda por conexões de entrada
    s.listen()

    # Aguarda por conexões e manipula-as
    while True:
        # Aceita a conexão de entrada
        conn, addr = s.accept()
        print('Conectado por', addr)

        # Lê os dados do cliente
        data = conn.recv(1024)
        if not data:
            break

        # Envia a resposta de volta para o cliente
        conn.sendall(b'Recebido: ' + data)

    # Fecha a conexão
    conn.close()
