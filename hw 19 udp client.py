#!/usr/bin/python
import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
	data=input("Type Something(q or Q to exit:)")
	if data=='q' or data=='Q':
		client_socket.close()
		break
	else:
		client_socket.sendto(bytes(data, encoding = "utf-8") ,("localhost", 8080))
		newdata=client_socket.recvfrom(512)
		print("Received:", newdata[0])