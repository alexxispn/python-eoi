import socket

HOST = '127.0.0.1'  # Dirección del host (localhost)
PORT = 65432  # Puerto donde escuchará (los puertos no reservados son > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # asocia el socket con el host y el puerto
    s.listen()  # establece el socket en model servidor
    conn, addr = s.accept()  # devuelve una conexión abierta entre el
    # servidor y el cliente, y la dirección del cliente
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(
                1024)  # recibe datos con una longitud máxima de 1024 bytes
            if not data:
                break
            print('Received from client: ', repr(data))
            server_message = input('Server: ')
            conn.sendall(server_message.encode('utf-8'))

