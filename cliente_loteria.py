import socket
import sys

cliente_loteria = socket.socket()
cliente_loteria.connect( ('192.168.1.45',8080) ) #Se conecta con el servidor_loteria
try:
    mensaje_server = cliente_loteria.recv(1024)#Aquí puedes obtener el mensaje que has escrito en el servidor.
    mensaje_numero_random = cliente_loteria.recv(1024)
    print(mensaje_server)
    print(mensaje_numero_random)
    #cliente_loteria.close()
    sys.exit(1)
except KeyboardInterrupt:
    print('Has abortado antes de saber si has ganado o no...')
    sys.exit(1)
