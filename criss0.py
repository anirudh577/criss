import socket

serverIP = '172.17.29.11'
serverPORT = 6000

serveraddress = (server,serverPORT)
bufferSize = 1024
UDPClinetSocket = socket.socket(family=socket.AP_INET, type=socket.SOCK_DGRAM )

message = 'python lite'

bytestosend =str.encode(message)

UDPClinetSocket.sendto(bytestosend,serveraddress)