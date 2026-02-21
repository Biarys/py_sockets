import socket

serverName = "localhost"
serverPort = 10002
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = r"GET /hello.txt HTTP/1.1\r\nUser-Agent: mozilla/147.0.3\r\nHost: localhost\r\nAccept-Language: en\r\n\r\n"
clientSocket.send(message.encode())
returnMessage, addr = clientSocket.recvfrom(2048)
print(f"From server: {returnMessage.decode()}")
clientSocket.close()
