from subprocess import PIPE,Popen

proceso = Popen("ipconfig",
                shell=True,
                stdout=PIPE,
                stdin = PIPE,
                stderr = PIPE
                )

salida,error = proceso.communicate()
   
salida_final =  salida + error

try:
    salida_final = salida_final.decode()
except UnicodeDecodeError:
    salida_final = salida_final.decode('windows-1252')

print(salida_final)