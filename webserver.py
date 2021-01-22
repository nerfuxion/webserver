#https://github.com/nerfuxion/webserver

import socket

SOMAXCONN = 128

serverIp = ""
serverPort = 80
inputBufferSize = 1024
defaultErrorFile = "www/404.html"

print("server active")

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((serverIp, serverPort))
serverSocket.listen(SOMAXCONN)

while(1 == 1):
    acceptSocket, acceptAddress = serverSocket.accept()
    incomingRequest = acceptSocket.recv(inputBufferSize)

    print("incoming request from ip: " + str(acceptAddress[0]) + " on port: " + str(acceptAddress[1]))

    incomingRequest = incomingRequest.decode("utf-8")
    requestedResource = incomingRequest.split(' ')
    requestedResource = requestedResource[1]
    requestedResource = requestedResource.split('HTTP')
    requestedResource = requestedResource[0]

    if(requestedResource == "/"):
        requestedResource = "/index.html"

    requestedResource = "www" + requestedResource

    print("requested resource: " + requestedResource)

    try:
        fileDescriptor = open(requestedResource, "rb")
    except:
        fileDescriptor = open(defaultErrorFile, "rb")

    fileContent = fileDescriptor.read()
    acceptSocket.send(fileContent)
    fileDescriptor.close()

    acceptSocket.close()

serverSocket.close()
