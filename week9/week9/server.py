from socket import *
import sys
import os
print("Current working directory:", os.getcwd())
# Create server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind ke port
serverPort = 6789
serverSocket.bind(('', serverPort))

# Listen koneksi
serverSocket.listen(1)

print("Server ready on port", serverPort)

while True: # loop utk terima koneksi
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        # Receive request
        message = connectionSocket.recv(1024).decode()
        print("Request:\n", message)

        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        # Kirim HTTP header
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Kirim isi file
        for i in range(len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.close()

    except IOError:
        # File tidak ditemukan
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())

        connectionSocket.close()

serverSocket.close()
sys.exit()