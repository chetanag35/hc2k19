from socket import *
servername='www.google.com'
serverport=80
clientsock=socket(AF_INET,SOCK_DGRAM)
msg=raw_input('input:')
clientsock.sendto(msg,(servername,serverport))
sermsg, serveraddr=clientsock.recvfrom(2048)
print sermsg
clientsock.close()