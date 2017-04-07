import socket

def main():
	msj = ""
	host,port = 'localhost',10000
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,port))
	while msj != "salir":		
		msj = input(">")
		s.send(msj.encode('utf-8'))
	s.close()

main()