#Halaa Menasy
#109316248


#import socket module
from socket import *

serverPort=6248
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverSocket.bind(('',serverPort))

#Fill in start
serverSocket.listen(1)

#Fill in end
print"the web server is on port",serverPort


while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()#Fill in start #Fill in end
    try:
        message =connectionSocket.recv(1024) #Fill in start #Fill in end
        # print message, '::', message.split()[0],':', message.split()[1]
        filename = message.split()[1]

        print filename, '||', filename[1]
        f = open(filename[1:],"r")

        outputdata = f.read()#Fill in start #Fill in end
        print outputdata

        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n")

        print "OK"

        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        print"404 Not Found"
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n")


serverSocket.close()
