from socket import *
serverName = 'localhost'
serverPort = 12000
# create client socket
serverSocket = socket(AF_INET, SOCK_STREAM)
# connect to server
serverSocket.connect((serverName, serverPort))
# send message to server
sentence = input('Input lowercase sentence: ')
serverSocket.send(sentence.encode())
# receive modified message from server
modifiedSentence = serverSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
# close the socket
serverSocket.close()
