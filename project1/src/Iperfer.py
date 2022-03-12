import socket
import sys
import time

if(len(sys.argv) != 4):
    print("Error: missing or additional arguments")
    quit()

serverHost=str(sys.argv[1])  

serverPort=int(sys.argv[2]) 

imputTime=int(sys.argv[3])

if((serverPort < 1024) or (serverPort > 65535)): 
    print("Error: port number must be in the range 1024 to 65535")
    quit()

connectionTo=(serverHost, serverPort)

clientSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(connectionTo)

dataSent=bytearray(1000) 

counter=0

timer=time.perf_counter()

while timer - time.perf_counter() < imputTime:
    clientSocket.send(dataSent)
    counter+=1
    continue

print("sent=", counter, " KB rate=", counter*8.0/10000.0, " Mbps")

clientSocket.close()
