#pylint: disable = W,C

# Aditya Balwani
# SBUID : 109353920
# CSE 310 Lab 4 Python Client

import sys, time
from socket import *
from datetime import datetime

# Get the server hostname and port as command line arguments
argv = sys.argv
host = argv[1]
port = argv[2]

# Create UDP client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Set socket timeout as 1 second
clientSocket.settimeout(2)

# Command line argument is a string, change the port into integer
port = int(port)

print "Pinging " + host+":"+str(port) + " with 10 packets"

# Init initial values
pingMin = 1
pingMax = 0
pingSum = 0
successCount = 0

for seqno in range(0,10):
# Fill in end

    # Format the message to be sent
    data = "Ping " + str(seqno) + " " + time.asctime()

    # Attempt to send and receive
    try:
	    # Record the sent time
        sntTime = time.time()

	    # Send the UDP packet with the ping message
        clientSocket.sendto(data,(host,port))

	    # Receive the server response
        modifiedSentence,sender = clientSocket.recvfrom(1024)
        clientSocket.settimeout(2)

        # Record the received time
        rcvTime = time.time()

        #Do required calculations
        responseTime = rcvTime - sntTime

        if pingMin > responseTime:
            pingMin = responseTime
        if pingMax < responseTime:
            pingMax = responseTime
        successCount += 1
        pingSum += responseTime


	    # Display the server address and server response as an output
        print "\nReply from " + str(sender) + "\nMessage : " + modifiedSentence

	    # Round trip time is the difference between sent and received time
        print "RTT: " + str(rcvTime - sntTime) + " seconds"

    except Exception,err:
        # print(err)
        # Server does not response
	# Assume the packet is lost
        print "\nRequest timed out."

# Close the client socket
clientSocket.close()

# Print statistics
print "\nMinimum Response Time : " + str(pingMin) + " seconds"
print "Maximum Response Time : " + str(pingMax) + " seconds"
print "Average Response Time : " + str(pingSum/successCount) + " seconds"
print "Success Rate : " + str(successCount*10) + "%"
