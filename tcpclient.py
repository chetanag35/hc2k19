from socket import *
serverport=2000
servername='localhost'
clsock=socket(AF_INET,SOCK_STREAM)
clsock.connect((servername,serverport))
msg=raw_input('input')
clsock.send(msg)
modmsg=clsock.recv(2048)
clsock.close()