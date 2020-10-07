#!/usr/bin/python3

def main():
	import secrets, math, string
	charset = string.ascii_uppercase
	charset += charset.lower()
	charset += string.digits
	charset += string.punctuation
	passwd = ''
	for i in range(16):
	    j = secrets.choice(charset)
	    passwd += j
	print("password is: ", passwd + '\n----------------\n')
	entropy = math.log2(len(charset)**len(passwd))
	possible_com = len(charset)**len(passwd)
	print('entropy is {} bits.\nPossible combinations are {} '.format(entropy, possible_com))

if __name__ == '__main__':
    main()
