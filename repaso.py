import os
os.system("cls")

######################################### repaso funciones  #######################################################
# from random import shuffle

# # lista inical

# palitos = ["-","--","---","----"]

# # Mezclar palitos

# def mezclar (palitos):
#     shuffle(palitos)
#     return palitos

# # pedir intento

# def probar_suerte ():
#     intento = int(input("ingresa un numero del 1 al 4:\n"))
#     while intento not in range(0,5):
#         intento = int(input("El numero debe ser del 0 al 4, ingresa un numero:\n"))
#     return intento

# # verificar intento

# def intento (palitos,intento):
#     if palitos[intento - 1] == "-":
#         print("Perdiste")
#     else:
#         print("Ganaste")
#     print(f"Te ha tocado el palito{palitos[intento - 1]}")

# palitos_mezclados = mezclar(palitos)
# seleccion = probar_suerte()
# intento(palitos_mezclados,seleccion)
# from random import *
# dado1 = 0
# dado2 = 0
# def lanzar (dado1,dado2):
#     dado1 = randint(1,6)
#     dado2 = randint(1,6)
#     print(dado1,dado2)
#     if dado1 + dado2 <= 6:
#         print(f"La suma de tus dados es {dado1 + dado2}. Lamentable")
#     elif dado1 + dado2 > 6 and dado1 + dado2 < 10:
#         print(f"La suma de tus dados es {dado1 + dado2}. Tienes buenas chances")
#     else:
#         print(f"La suma de tus dados es {dado1  + dado2}. Parece una jugada ganadora")
# print(lanzar(dado1,dado2))

# lista_numeros = [1,2,15,7,2,8]
 
# def reducir_lista(lista):
#     lista = list(set(lista))
#     lista.sort()
#     lista.pop(-1)
#     return lista
 
# def promedio(lista):
#     valor_medio = sum(lista)/len(lista)
#     return valor_medio

# def lanzar_moneda():
#     resultado = random.choice(["Cara", "Cruz"])
#     return resultado
 
# def probar_suerte(moneda, lista):
#     if moneda == "Cara":
#         print("La lista se autodestruirá")
#         return []
#     elif moneda == "Cruz":
#         print("La lista fue salvada")
#         return lista

# from random import *

# lista_numeros = [1,2,15,7,2,8]
# eleccion = ["Cara","Sello"]
# def lanzar_moneda (eleccion):
#     eleccion = choice(eleccion)
#     if eleccion == "Cara":
#         print(f"El resultado fue: {eleccion}")
#         print("La lista se auto destruira")
#         print([])
#         return []
#     else:
#         print(f"El resultado fue: {eleccion}")
#         print("La lista fue salvada")
#         print(lista_numeros)
#         return lista_numeros
# lanzar_moneda(eleccion)

# def suma_cuadrados (*args):
#     suma = 0
#     for arg in args:
#         suma = suma + arg**2
#     print(suma)
#     return(suma)
# suma_cuadrados(3,6)

# def suma_absolutos (*args):
#     resultado = 0
#     for numero in args:
#         resultado = resultado + abs(numero)
#     return(resultado)
# suma_absolutos(-2,3,4,-6)

def numeros_persona (nombre,*args):
    nombre = input("Ingresa tu nombre")
    suma_numeros = sum(args)
    print(f"{nombre}, la suma de tus números es {suma_numeros}")
    return(f"{nombre}, la suma de tus números es {suma_numeros}")
numeros_persona(1,2,6)





    

