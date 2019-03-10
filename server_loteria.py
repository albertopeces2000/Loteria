import socket
import sys
import random

#print(random.randrange(10)
def IP_PORT():
    IP = input('Introduce una IP: ')
    PORT = int(input('Introduce un PORT: '))
    return IP,PORT

IP,PORT = IP_PORT()

##############################################################
servidor_loteria = socket.socket()
servidor_loteria.bind( (IP, PORT) )
servidor_loteria.listen(5) #He puesto un número arbitrario.

conexion, address = servidor_loteria.accept()# devuelve dos tuplas. Una la IP y la otra el puerto correspondiente.
print('Nueva conexión establecida. El servidor está analizando datos...')
print('Esta es la IP del concursante:',address)
#De la línea 12-19 es solo la inicialización del servidor.
###############################################################
lista_address = list(address)
#a = ['192.168.1.45', 57327]
IP_address = lista_address[0].replace("'","")
list_aux = IP_address.replace(".",',').split(',')
list_IP = []
for ip_number in list_aux:
    ip_number = int(ip_number)
    list_IP.append(ip_number)
#De la línea 23-31 los distintos números de la ip los meto en una lista por separado para su futura operación.
#################################################################
suma = sum(list_IP)
resto = suma % 10
print(resto)
#print(random.randrange(10)) # Del 0-9
random_number = random.randrange(10)
print(random_number)
##################################################################
repetir = True
while repetir:
    try:
        if resto == random_number:
            message_server = str.encode('ENHORABUENA, TE HA TOCADO LA LOTERIA!!!. Su numero era: ')
            message_random_number = str.encode(str(random_number))#Aquí cambiamos el formato de int a str y de str a byte.
            conexion.send(message_server)#Aquí enviamos al cliente la información
            conexion.send(message_random_number)#Aquí enviamos al cliente el número aleatorio
###################################################################
            IP,PORT = IP_PORT()

##############################################################
            servidor_loteria = socket.socket()
            servidor_loteria.bind( (IP, PORT) )
            servidor_loteria.listen(5) #He puesto un número arbitrario.

            conexion, address = servidor_loteria.accept()# devuelve dos tuplas. Una la IP y la otra el puerto correspondiente.
            print('Nueva conexión establecida. El servidor está analizando datos...')
            print('Esta es la IP del concursante:',address)
#De la línea 52-59 es solo la inicialización del servidor.
###############################################################
            lista_address = list(address)

            IP_address = lista_address[0].replace("'","")
            list_aux = IP_address.replace(".",',').split(',')
            list_IP = []
            for ip_number in list_aux:
                ip_number = int(ip_number)
                list_IP.append(ip_number)
#De la línea 61-69 los distintos números de la ip los meto en una lista por separado para su futura operación.
            suma = sum(list_IP)
            resto = suma % 10
            print(resto)
            random_number = random.randrange(10)
            print(random_number)

            repetir = True

        else:
            message_server = str.encode('Lo sentimos, no ha ganado la loteria. Su numero aleatorio era: ')
            message_random_number = str.encode(str(random_number))
            conexion.send(message_server)#Aquí enviamos al cliente la información
            conexion.send(message_random_number)#Aquí enviamos al cliente el número aleatorio
###################################################################
            IP,PORT = IP_PORT()
##############################################################
            servidor_loteria = socket.socket()
            servidor_loteria.bind( (IP, PORT) )
            servidor_loteria.listen(5) #He puesto un número arbitrario.

            conexion, address = servidor_loteria.accept()# devuelve dos tuplas. Una la IP y la otra el puerto correspondiente.
            print('Nueva conexión establecida. El servidor está analizando datos...')
            print('Esta es la IP del concursante:',address)
#De la línea 85-92 es solo la inicialización del servidor.
###############################################################
            lista_address = list(address)

            IP_address = lista_address[0].replace("'","")
            list_aux = IP_address.replace(".",',').split(',')
            list_IP = []
            for ip_number in list_aux:
                ip_number = int(ip_number)
                list_IP.append(ip_number)
#De la línea 94-102 los distintos números de la ip los meto en una lista por separado para su futura operación.
            suma = sum(list_IP)
            resto = suma % 10
            print(resto)
            random_number = random.randrange(10)
            print(random_number)

            repetir = True

    except ConnectionAbortedError:
        servidor_loteria.close()
        print('El servidor se está cerrando...')
        repetir = False

    except KeyboardInterrupt:

        conexion.close() #Cerramos la conexion de la IP
        servidor_loteria.close() #Cerramos el servidor
        print('El servidor se está cerrando...')

        repetir = False
