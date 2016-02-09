#Halaa Menasy
#109316248


#import socket module
from socket import *

#sets port
serverPort = 6248
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverSocket.bind(('',serverPort))

#tells the socket to listen for requests
serverSocket.listen(1)


#print"the web server is on port",serverPort


while True:
    #Establish the connection
    print 'Ready to serve...'

    connectionSocket, addr = serverSocket.accept()#creates a socket for this specific client


    try:
        message = connectionSocket.recv(1024) #recieves message from client

        filename = message.split()[1]

        f = open(filename[1:]) #opens file and reads the contents

        outputdata =f.read()

        #send one HTTP headerline to socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
        print 'File Recieved'


    except IOError:
        #Send response message for file not found
        print"404 Not Found"
        connectionSocket.send('\HTTP/1.1 404 Not Found \n\n')
        connectionSocket.close()


serverSocket.close()
