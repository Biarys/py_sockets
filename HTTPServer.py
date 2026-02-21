import os
import socket

serverPort = 10002
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("server is ready")


while True:
    connSocket, addr = serverSocket.accept()
    message = connSocket.recv(2048).decode()
    print(f"client addr: {addr}. message: {message}")

    request_line = message.split(r"\r\n")[0]
    method, path, _ = request_line.split(" ")
    path = "."+path
    if method.upper() not in ["GET", "POST", "PUT", "DELETE"]:
        header = "HTTP/1.1 405 Method Not Allowed"
        connSocket.send(header.encode())
    
    elif os.path.exists(path):
        file_size = os.path.getsize(path)
        header = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            f"Content-Length: {file_size}\r\n"
            "Connection:close\r\n"
            "\r\n"
        )
        # connSocket.send(header.encode())
        body = open(path, "rb").read()
        connSocket.send(header.encode() + body)
    else:
        header = "HTTP/1.1 404 Not Found"
        connSocket.send(header.encode())



    connSocket.close()