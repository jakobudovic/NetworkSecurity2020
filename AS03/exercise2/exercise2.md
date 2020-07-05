# Assignment 3

## Exercise 2

With *protknocking* (slide 54, [lecture 3](https://youtu.be/Xhm-NWz8kVY?t=6905), 1:55 )


We said you can send udp packets to ports 42, 53, 4000 and 666 from IP 1.2.3.4 and open SSH connection in that way.  
It would not be visible to port scanners.

53, 80, 443

You can bind ssh (port 22) to the 443 (https) for example. Also to port 53 if you want.  
Port 80 would normaly block anything that's not HTTP.

42, 53, 4000, 666


$ cat /etc/services 

42:  
53: TCP, DNS  
80: Http  
443: Https  
4000: ?  
666: ?  

