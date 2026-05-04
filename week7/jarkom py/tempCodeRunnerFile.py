try:
    while True:
        connectionSocket, addr = serverSocket.accept()
        print('Connected by', addr)
        sentence = connectionSocket.recv(1024).decode()
        print('Received from client:', sentence)
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode())
        connectionSocket.close()
except KeyboardInterrupt:
    print('Server is shutting down.')
finally:
    serverSocket.close()