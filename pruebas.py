import os
os.system("cls")
from random import *

# # crear lista

# palitos = ["-","--","---","----"]

# # mezclar palitos

# def mezclar (palitos):
#     shuffle(palitos)
#     return palitos

# # pedir intento

# def intento ():
#     intento = input("Ingrese un numero del 1 al 4:\n")
#     while intento not in ["1","2","3","4"]:
#         intento = input("numero incorrecto debe ser del 1 al 4:\n")
#     return int(intento)

# # chequear intento

# def revisar_intento(palitos,intento):
#     if palitos[intento - 1] == "-":
#         print("perdiste")
#     else:
#         print("te salvaste")
#     print(f"te ha tocado el palito {palitos[intento -1]}")

# mezcla = mezclar(palitos)
# seleccion = intento()
# revisar_intento(mezcla,seleccion)

# dado1 = randint(1,6)
# dado2 = randint(1,6)

# def lanzar_dados (dado1,dado2):
#     return (dado1,dado2)

# def evaluar_jugada (dado1,dado2):
#     suma_dados = dado1 + dado2
#     if suma_dados < 6:
#         return(f"La suma de tus dados es {suma_dados}. Lamentable") 
#     elif suma_dados >= 6 and suma_dados < 10:
#         return(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
#     elif suma_dados >= 10:
#         return(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")
#     else:
#         pass
# print(evaluar_jugada(dado1,dado2))

# def devolver_distintos(num1,num2,num3):
#     resultado = num1 + num2 + num3
#     numeros = [num1,num2,num3]
#     if resultado > 15:
#         return max(numeros)
#     elif resultado < 10:
#         return min(numeros)
#     else:
#         numeros.sort()
#         return numeros[1]
# print(devolver_distintos(7,2,4))


