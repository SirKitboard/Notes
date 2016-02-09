# pylint: disable=W,C

# Aditya Balwani, SBUID : 109353920

#import socket module
from socket import *
serverPort = 8920
serverSocket= socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print "hello"
while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()
    print "hi"
    try:
        print "hi2"
        message = connectionSocket.recv(2048)
        print "hi3"
        print message

        filename = message.split()[1]
        print filename

        fileType = filename.split(".")[1].lower()
        print fileType

        f = open(filename[1:],"r")
        outputdata = f.read()
        #Send one HTTP header line into socket
        #Fill in start

        # Check file types
        if fileType == 'jpg' or fileType == 'jpeg':
            contentType = 'image/jpeg'
        elif fileType == 'png':
            contentType = 'image/png'
        elif fileType == 'html':
            contentType = 'text/html'
        else:
            contentType = 'text/plain'

        print contentType

        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: "+contentType+"; charset=utf-8\r\n\r\n")
        print f
        #Fill in end
        #Send the content of the requested file to the client
        for line in outputdata:
            #print line
            connectionSocket.send(line)
        connectionSocket.close()
    except IOError:
        #Sendresponse message for file not found
        #Fill in start
        connectionSocket.send("HTTP/1.1 404 NOT FOUND\r\nContent-Type: text/html; charset=utf-8\r\n\r\n")
        print "HIIIIIII"
        connectionSocket.send("<html><head><title>Hi</title></head><body><h1>404 NOT FOUND</h1></body></html>")
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
serverSocket.close()
