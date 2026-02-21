import socket

serverName = "localhost"
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("input message in lowercase: ")
clientSocket.sendto(message.encode(), (serverName, serverPort))
returnedMessage, serverAddress = clientSocket.recvfrom(2048)
print(returnedMessage.decode())
clientSocket.close()