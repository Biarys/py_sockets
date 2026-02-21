import socket

serverPort = 10001
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("server is ready")
while True:
    connSocket, addr = serverSocket.accept()
    message = connSocket.recv(2048).decode()
    print(f"client addr: {addr}. message: {message}")
    modifiedMessage = message.upper()
    connSocket.send(modifiedMessage.encode())
    connSocket.close()