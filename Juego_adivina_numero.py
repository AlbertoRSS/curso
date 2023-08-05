
from random import randint
nombre = input("indica tu nombre:\n")
num_correcto = randint(1,100)
num = 0
intentos = 0

print(F"Bueno {nombre} he pensado un numero entre 1 y 100 y tienes solo ocho intentos para adivinar cuál crees que es el número ?")

while intentos < 8:
    num = int(input("cual es el numero?: "))
    intentos += 1

    if num < 0 and num > 100:
        print("Has elegido un número que no está permitido.")
    elif num < num_correcto:
        print("Casi!!! El numero es menor al número secreto")
    elif num > num_correcto:
        print("estas cerca!!! El numero es mayor al número secreto")
    else:
        print(f"!!!Felicidades {nombre}, el numero era {num_correcto} y lo has hecho en {intentos} intentos")
        break
if num != num_correcto:
    print(f"Lo siento {nombre}, se ha agotado el  numero de intentos el numero secreto era {num_correcto}")               
