#VRFY SMNP Script to enumerate for users on a system

#!/usr/bin/python3
import socket, sys

def main():
	#create socket (IPv4 and TCP)
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	#connect to target
	conn=s.connect((sys.argv[1],25))

	#Receive banner and print
	banner=s.recv(1024)
	print(banner.decode())

	#Open file supplied
	f = open(sys.argv[2])

  	#VRFY users
	for i in f:
		str='VRFY ' + i + '\r'
		s.send(str.encode())
		result=s.recv(1024)
		if "252" in result.decode():
			print("valid user: " + i)

#boiler plate
if __name__ == '__main__':
	main()
