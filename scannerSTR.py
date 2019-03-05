import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('cls',shell=True)

servidor=input("Ingresa el nombre del servidor: ")
servidorIP=socket.gethostbyname(servidor)
print("Espera mientras se esta escaneando")

t1=datetime.now()

def scanner(puerto):
	try:
		sock.connect((servidorIP,puerto))
		return True
	except:
		return False

try:

	for puerto in [25, 80, 443]:
		sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		#result=sock.connect((servidorIP,port))
		print("Escaneando puerto", puerto)
		if scanner(puerto):
			print ("Puerto", puerto ," esta abierto")
		sock.close()
	
except KeyboardInterrupt:
	print("Presionaste ctrl + c")
	sys.exit()
	
except socket.gaierror():
	print("No se resolvio el host")
	
except socket.error():
	print("No se pudo conectar al servidor")
	
t2=datetime.now()
total=t2-t1
print("Escaneo completado en", total)