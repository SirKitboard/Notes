# CSE  Lab 4
## WireShark TCP Lab
## Aditya Balwani, SBUID : 109353920
### Part 1

1.	**What is the IP address of your host? What is the IP address of the destination host?**

  My IP Address is 130.245.23.108. The IP address of the destination host is 143.89.14.2<br/><br/><br/>

2. **Why is it that an ICMP packet does not have source and destination port numbers?**

  The ICMP Packet doesn't have a source and destination port number because it is designed to communicate between the network layer and not the application layer.<br/><br/><br/>

3. **Examine one of the ping request packets sent by your host. What are the ICMP type and code numbers? What other fields does this ICMP packet have? How many bytes are the checksum, sequence number and identifier fields?**

  * The ICMP Type is 8
  * THE ICMP Code number is 0
  * The checksum is 16 bytes
  * Sequence numbers:
    * BE is 16 bytes
    * LE is 16 bytes
  * Identifiers
    * BE is 16 bytes
    * LE is 16 bytes<br/><br/><br/>

  <div class="page-break"></div>

4. **Examine the corresponding ping reply packet. What are the ICMP type and code numbers? What other fields does this ICMP packet have? How many bytes are the checksum, sequence number and identifier fields?**

  * The ICMP Type is 0
  * THE ICMP Code number is 0
  * The checksum is 16 bytes
  * Sequence numbers:
    * BE is 16 bytes
    * LE is 16 bytes
  * Identifiers
    * BE is 16 bytes
    * LE is 16 bytes<br/><br/><br/>

  ![](img/1.PNG)

  <div class="page-break"></div>

  ![](img/3.PNG)<br/><br/><br/>

  ![](img/4.PNG)


  <div class="page-break"></div>

  ### Part 2

5. **What is the IP address of your host? What is the IP address of the target destination host?**

  My IP Address is 130.245.23.108. The IP address of the destination host is 128.93.162.84<br/><br/><br/>

6. **If ICMP sent UDP packets instead (as in Unix/Linux), would the IP protocol number still be 01 for the probe packets? If not, what would it be?**

  No if ICMP sent UDP packets, the IP protocol number would then be 11<br/><br/><br/>

7. **Examine the ICMP echo packet in your screenshot. Is this different from the ICMP ping query packets in the first half of this lab? If yes, how so?**

  The echo packet has the same fields as the query packet<br/><br/><br/>

8. **Examine the ICMP error packet in your screenshot. It has more fields than the ICMP echo packet. What is included in those fields?**

  The error packet contains the IP header of the original packet and the original ICMP packet<br/><br/><br/>

  ![](img/5.PNG)

  ![](img/6.PNG)<br/><br/><br/>

9. **Examine the last three ICMP packets received by the source host. How are these packets different from the ICMP error packets? Why are they different?**

  The last 3 ICMP packets received are Ping replies (type 0) instead of TTL Expired (type 11) because the packets have made their way to the destination<br/><br/><br/>

10. **Within the tracert measurements, is there a link whose delay is significantly longer than others? Refer to the screenshot in Figure 4, is there a link whose delay is significantly longer than others? On the basis of the router names, can you guess the location of the two routers on the end of this link?**

  Within the tracert measurements, the link between step 5 to 6 has a significantly longer delay than others.

  In figure 4, the link from step 9 to 10 has a delay significantly longer than others. This is the link from NYC to Pastourelle, France

  ![](img/2.PNG)

  ![](img/7.PNG)<br/><br/><br/>
