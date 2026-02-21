import socket

serverName = "localhost"
serverPort = 10001
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = input("input lowercase message: ")
clientSocket.send(message.encode())
returnMessage, addr = clientSocket.recvfrom(2048)
print(f"From server: {returnMessage.decode()}")
clientSocket.close()
