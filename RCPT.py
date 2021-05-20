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

	if "503" in result.decode():
	  str='HELO muzz' + '\r\n'
		s.send(str.encode())
		result=s.recv(1024)
		print(result.decode())
		str='MAIL FROM: <muzz@test.com>' + '\r\n'
		s.send(str.encode())
		result=s.recv(1024)
		print(result.decode())
		f = open("emails.txt")
		for i in f:
			str='RCPT TO: <' + i + '>\r\n'
			s.send(str.encode())
			result=s.recv(1024)
			if "250" in result.decode():
				print("valid email: " + i)
		f.close()
		s.close()
	else:
		s.close()

#boiler plate
if __name__ == '__main__':
	main()
