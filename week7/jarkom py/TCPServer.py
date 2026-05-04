from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
try:
    while True:
        try:
            connectionSocket, addr = serverSocket.accept()
            print('Connected by', addr)
            sentence = connectionSocket.recv(2048).decode()
            print('Received from client:', sentence)
            capitalizedSentence = sentence.upper()
            connectionSocket.send(capitalizedSentence.encode())
            connectionSocket.close()
        except Exception as e:
            print('Error handling client:', e)
except KeyboardInterrupt:
    print('Server is shutting down.')
finally:
    serverSocket.close()

