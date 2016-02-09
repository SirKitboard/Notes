# CSE  Lab 3

## I. WireShark HTTP Lab

## Aditya Balwani, SBUID : 109353920

### Part 1
<ol>
<li>**Run nslookup to obtain the IP address of a Web server in Asia. What is the IP address of that server?** <br/><br/>

<img src="img/1.PNG"/>

<br/><br/></li>
<li>**Run nslookup to determine the authoritative DNS servers for a university in Europe.** <br/><br/>

<img src="img/2.PNG"/>
</li>
<li>**Run nslookup so that one of the DNS servers obtained in Question s queried for the mail servers for Yahoo! mail. What is its IP address?** <br/><br/>

The IP address is 98.139.21.169

<img src="img/3_re2.PNG"/>

<br/><br/></li>
<li>**Locate the DNS query and response messages. Are then sent over UDP or TCP?** <br/><br/>

The query and response were sent over UDP.

<br/><br/></li>
<li>**What is the destination port for the DNS query message? What is the source port of DNS response message?** <br/><br/>

The destination port of the request is 53. The source port of the response is 53

<br/><br/></li>
<li>**To what IP address is the DNS query message sent? Use ipconfig to determine the IP address of your local DNS server. Are these two IP addresses the same?** <br/><br/>

The DNS query message is sent to 130.245.9.242. Yes this is the address of my local DNS Server as seen in ipconfig :<br/><br/>

<img src="img/ipconfig.PNG"/>

<br/><br/></li>
<li>**Examine the DNS query message. What “Type” of DNS query is it? Does the query message contain any “answers”?** <br/><br/>

It is a standard type A query and does not contain any answers

<br/><br/></li>
<li>**Examine the DNS response message. How many “answers” are provided? What do each of these answers contain?** <br/><br/>

The response contains 3 answers and each one contains the name, the canonical name, time to live and the data length. One of them also the contains an IP address

<br/><br/></li>
<li>**Consider the subsequent TCP SYN packet sent by your host. Does the destination IP address of the SYN packet correspond to any of the IP addresses provided in the DNS response message?** <br/><br/>

Yes, the destination of the IP Address of th destination corresponds to one of the IPs provided in the answers of the DNS Response

<br/><br/></li>
<li> **This web page contains images. Before retrieving each image, does your host issue new DNS queries?** <br/><br/>

No, the host does not issue more DNS queries because the images are hosted at the same domain. If the images were hosted somewhere else then it would issue new DNS queries.

<img src="img/q4-full.PNG"/>

<img src="img/q5.PNG"/>

<img src="img/q6.PNG"/>

<div class="page-break"></div>
</li>
<li> **What is the destination port for the DNS query message? What is the source port of DNS response message?** <br/><br/>

The destination port of the request is 53. The source port of the response is 53

<br/><br/></li>
<li> **To what IP address is the DNS query message sent? Is this the IP address of your default local DNS server?** <br/><br/>

The DNS query message is sent to 130.245.9.242. Yes this is the address of my local DNS Server as seen in ipconfig :<br/><br/>
<img src="img/ipconfig.PNG"/>

<br/><br/></li>
<li> **Examine the DNS query message. What “Type” of DNS query is it? Does the query message contain any “answers”?** <br/><br/>

It is a type A query and doesn't contain any answers.

<br/><br/></li>
<li> **Examine the DNS response message. How many “answers” are provided? What do each of these answers contain?** <br/><br/>

The response contains 3 answers and each one contains the name, the canonical name, time to live and the data length. One of them also the contains an IP address

<br/><br/></li>
<li> **Provide a screenshot. (indicating query and response messages)** <br/><br/>
<img src="img/q11.PNG"/>
<br/><br/>
<img src="img/q12.PNG"/>
<br/><br/></li>
<li> **To what IP address is the DNS query message sent? Is this the IP address of your default local DNS server?** <br/><br/>

The DNS query message is sent to 130.245.9.242. Yes this is the address of my local DNS Server as seen in ipconfig :<br/><br/>
<img src="img/ipconfig.PNG"/>

<br/><br/></li>
<li> **Examine the DNS query message. What “Type” of DNS query is it? Does the query message contain any “answers”?** <br/><br/>

It is an NS Type query, and it does not contain any answers

<br/><br/></li>
<li> **Examine the DNS response message. What MIT nameservers does the response message provide? Does this response message also provide the IP addresses of the MIT namesers?** <br/><br/>

The reponse provides 2 name servers which are www.mit.edu.edgekey.net and e9566.dscb.akamaiedge.net. No it does not provide the IP address for the nameservers.

<br/><br/></li>
<li> **Provide a screenshot. Indicate query and response messages** <br/><br/>

<img src="img/q16.PNG"/>
<img src="img/q17.PNG"/>

<br/><br/></li>
<li> **To what IP address is the DNS query message sent? Is this the IP address of your default local DNS server? If not, what does the IP address correspond to?** <br/><br/>

NOTE : Using the university of Seoul National University domain which is www.snu.ac.kr and using Google DNS (8.8.8.8) as the DNS server

The DNS Query is sent to 8.8.8.8 which corresponds to Google's DNS. No this is not the default dns.

<br/><br/></li>
<li> **Examine the DNS query message. What “Type” of DNS query is it? Does the query message contain any “answers”?** <br/><br/>

It is a standard type A query and does not contain any answers.

<br/><br/></li>
<li> **Examine the DNS response message. How many “answers” are provided? What does each of these answers contain?** <br/><br/>

There are 2 answers provided the first one is the canonical name and the second has the address.

<br/><br/></li>
<li> **Provide a screenshot. Indicate query and response messages**

<img src="img/q20.PNG"/>

<img src="img/q21.PNG"/>

<br/><br/></ol>

### Part 2

#### Documentation

This is a simple HTTP server written in python. It can handle files of type html, rawtext, jpeg and pngs. To execute the server, simply run `python part3server.py` on an allv machine and then visit [http://allv24.all.cs.stonybrook.edu:8920/Hello,html]()

#### Server code :

```python
# pylint: disable=W,C

#Aditya Balwani, SBU ID : 109353920

#import socket module
from socket import *
#Set port number to 8920
serverPort = 8920
serverSocket= socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket, bind port
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
while True:
    #Establish the connection
    print 'Ready to serve...'

    #Accept a request from a host
    connectionSocket, addr = serverSocket.accept()
    try:
        #On request recieved, parse the message
        message = connectionSocket.recv(2048)
        print message

        #Extract the filename and the filetype
        filename = message.split()[1]
        print filename

        fileType = filename.split(".")[1].lower()
        print fileType

        #Read file type
        f = open(filename[1:],"r")
        outputdata = f.read()

        # Check file types, and define content type header
        if fileType == 'jpg' or fileType == 'jpeg':
            contentType = 'image/jpeg'
        elif fileType == 'png':
            contentType = 'image/png'
        elif fileType == 'html':
            contentType = 'text/html'
        else:
            contentType = 'text/plain'

        print contentType

        # Send HTTP OK
        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: "+contentType+"; charset=utf-8\r\n\r\n")

        #Send the content of the requested file to the client
        for line in outputdata:
            #print line
            connectionSocket.send(line)
        connectionSocket.close()
    except IOError:
        #Sendresponse message for file not found
        connectionSocket.send("HTTP/1.1 404 NOT FOUND\r\nContent-Type: text/html; charset=utf-8\r\n\r\n")

        # Send a 404 page
        connectionSocket.send("<html><head><title>Hi</title></head><body><h1>404 NOT FOUND</h1></body></html>")
        #Close client socket

        connectionSocket.close()

serverSocket.close()

```

<div class="page-break"></div>

#### Screenshots
<img src="img/Screen1.png"/>
<img src="img/Screen2.png"/>
<img src="img/Screen3.png"/>
