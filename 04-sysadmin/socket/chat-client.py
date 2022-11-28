import socket

HOST = '127.0.0.1'  # Dirección del host (localhost)
PORT = 65432  # Puerto donde transmitirá (el del server)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # conecta el socket a la dirección remota.
    while True:
        string = input('> ')  # solicita al usuario datos por consola
        s.sendall(string.encode('utf-8'))  # envía los datos al cliente
        data = s.recv(
            1024)  # recibe datos con una longitud máxima de 1024 bytes

        if data == b'exit':
            break
        print('Received', repr(data))
