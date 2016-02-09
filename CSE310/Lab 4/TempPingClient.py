import sys, time
from socket import *

# Get the server hostname and port as command line arguments
argv = sys.argv                      
host = argv[1]
port = argv[2]
 
# Create UDP client socket
# Fill in start			# Fill in end 

# Set socket timeout as 1 second
# Fill in start 		# Fill in end

# Command line argument is a string, change the port into integer
port = int(port)  
# Sequence number of the ping message
seqno = 0  

# Ping for 10 times
# Fill in start

# Fill in end

    # Format the message to be sent
    data = "Ping " + str(seqno) + " " + time.asctime()
    
    # Attempt to send and receive 
    try:
	# Record the sent time
        sntTime = # Fill in start			# Fill in end

	# Send the UDP packet with the ping message
        # Fill in start			# Fill in end
        
	# Receive the server response
        # Fill in start			# Fill in end
        
	# Record the received time
        rcvTime = # Fill in start			# Fill in end
        
	# Display the server address and server response as an output
        print "Reply from " + # Fill in start		# Fill in end 

	# Round trip time is the difference between sent and received time
        print "RTT: " + str(rcvTime - sntTime)

    except:
        # Server does not response
	# Assume the packet is lost
        print "Request timed out."

	# Continue the loop
        # Fill in start			# Fill in end
        

# Close the client socket
# Fill in start			# Fill in end
 
