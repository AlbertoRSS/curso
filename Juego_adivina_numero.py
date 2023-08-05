# from random import randint
# nombre = input("indica tu nombre:\n")
# print(F"Bueno {nombre} he pensado un numero entre 1 y 100 y tienes solo ocho intentos para adivinar cuál crees que es el número ?")
# numero = []
# num_correcto = randint(1,100)
# intentos = 8

# numero.append(int(input("Ingresa el primero numero: ")))
# if numero[0] == num_correcto:
#     print("Has ganado el desafio y te ha tomado solo 1 intento 'felicitaciones'")
# elif numero[0] < num_correcto:
#     print("has elegido un número menor al número secreto")
# elif numero[0] > num_correcto:
#     print("has elegido un número mayor al número secreto")
# elif numero[0] < 0 or numero > 100:
#     print("has elegido un número que no está permitido.")
# numero.append(int(input("Ingresa el segundo numero: ")))
# if numero[1] == num_correcto:
#     print("Has ganado el desafio y te ha tomado solo 2 intento 'felicitaciones'")
# elif numero[1] < num_correcto:
#     print("has elegido un número menor al número secreto")
# elif numero[1] > num_correcto:
#     print("has elegido un número mayor al número secreto")
# elif numero[1] < 0 or numero > 100:
#     print("has elegido un número que no está permitido.")
# numero.append(int(input("Ingresa el tercer numero: ")))
# if numero[2] == num_correcto:
#     print("Has ganado el desafio y te ha tomado solo 3 intento 'felicitaciones'")
# elif numero[2] < num_correcto:
#     print("has elegido un número menor al número secreto")
# elif numero[2] > num_correcto:
#     print("has elegido un número mayor al número secreto")
# elif numero[2] < 0 or numero > 100:
#     print("has elegido un número que no está permitido.")
# numero.append(int(input("Ingresa el cuarto numero: ")))
# if numero[3] == num_correcto:
#     print("Has ganado el desafio y te ha tomado solo 4 intento 'felicitaciones'")
# elif numero[3] < num_correcto:
#     print("has elegido un número menor al número secreto")
# elif numero[3] > num_correcto:
#     print("has elegido un número mayor al número secreto")
# elif numero[3] < 0 or numero > 100:
#     print("has elegido un número que no está permitido.")
# numero.append(int(input("Ingresa el quinto numero: ")))
# if numero[4] == num_correcto:
#     print("Has ganado el desafio y te ha tomado 5 intento 'felicitaciones'")
# elif numero[4] < num_correcto:
#     print("has elegido un número menor al número secreto")
# elif numero[4] > num_correcto:
#     print("has elegido un número mayor al número secreto")
# elif numero[4] < 0 or numero > 100:
#     print("has elegido un número que no está permitido.")
# numero.append(int(input("Ingresa el sexto numero: ")))
# if numero[5] == num_correcto:
#     print("Has ganado el desafio y te ha tomado 6 intento 'felicitaciones'")
# elif numero[5] < num_correcto:
#     print("has elegido un número menor al número secreto")
# elif numero[5] > num_correcto:
#     print("has elegido un número mayor al número secreto")
# elif numero[5] < 0 or numero > 100:
#     print("has elegido un número que no está permitido.")
# numero.append(int(input("Ingresa el septimo numero: ")))
# if numero[6] == num_correcto:
#     print("Has ganado el desafio y te ha tomado 7 intento 'felicitaciones'")
# elif numero[6] < num_correcto:
#     print("has elegido un número menor al número secreto")
# elif numero[6] > num_correcto:
#     print("has elegido un número mayor al número secreto")
# elif numero[6] < 0 or numero > 100:
#     print("has elegido un número que no está permitido.")
# numero.append(int(input("Ingresa el octavo numero: ")))
# if numero[7] == num_correcto:
#     print("Has ganado el desafio y te ha tomado 8 intento 'felicitaciones'")
# elif numero[7] < num_correcto:
#     print("has elegido un número menor al número secreto")
# elif numero[7] > num_correcto:
#     print("has elegido un número mayor al número secreto")
# elif numero[7] < 0 or numero > 100:
#     print("has elegido un número que no está permitido.")
# print(F"Ya no te quedan intentos {nombre}, el numero corecto era {num_correcto}, 'buena suerte para la proxima'")






################################################ 2da forma ###################################################
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