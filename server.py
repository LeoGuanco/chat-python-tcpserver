import socket,socketserver
import threading
import time

class MiTcpHandler(socketserver.BaseRequestHandler):
	"""docstring for MiTcpHandler"""

	def handle(self):
		data = ""
		while data != 'salir':
			data = self.request.recv(1024)
			print(data)
			time.sleep(0.1)


class ThreadServer(socketserver.ThreadingMixIn,socketserver.ForkingTCPServer):
	"""docstring for ThreadServer"""
	pass


def main():
	host,port = "localhost",10000
	server = ThreadServer((host,port), MiTcpHandler)
	server_thread = threading.Thread(target = server.serve_forever)
	server_thread.start()
	print("server corriendo")

main()