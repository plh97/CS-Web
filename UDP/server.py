from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('server is ready to receive')

while True:
  message, clientAddress = serverSocket.recvfrom(2048)
  modifyMessage = message.decode().upper()
  serverSocket.sendto(modifyMessage.encode(), clientAddress)