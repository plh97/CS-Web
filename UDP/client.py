from socket import *
serverName = 'hostname'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Input lowercase senence:')
clientSocket.sendto(message.encode(), (serverName,serverPort))
modifyMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifyMessage.decode())
clientSocket.close()