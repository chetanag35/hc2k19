from socket import *
serverport=2000
serversock=socket(AF_INET,SOCK_DGRAM)
serversock.bind(('',serverport))
print "Ready..."
while 1:
    msg, claddr=serversock.recvfrom(2048)
    modmsg= msg.upper()
    serversock.sendto(modmsg,claddr)