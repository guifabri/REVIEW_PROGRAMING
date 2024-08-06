import os
import platform
import sys


def clear_cls():
    """Use the clear terminal function for Linux or Windows"""
    sistema_operativo = platform.system()
    if sistema_operativo == "Windows":
        os.system('cls')
    elif sistema_operativo == "Linux":
        os.system('clear')
    else:
        print("Undetermined OS")
def saludo():
    print("Hola bienvenido a la calculadora mas avanzada del mundo")
    input("")
    clear_cls()
def raiz_cuadrada():
    numero = int(input("A que numero desea hallarle la raiz cuadrad: "))
    total = numero ** (1/2)
    print(f"La raiz cuadrada de {numero} es {total}")
    input("")
    clear_cls()
resp=""
while(resp!="7"):
    print("MENU")
    print("1.sumar numeros")
    print("2.restar numeros ")
    print("3.multplicar numeros")
    print("4.dividir numeros")
    print("5.Saludo")
    print("6.Raiz cuadrada")
    print("7.salir")
    
    resp=input("\n\t\6")
    
    if(resp!="7" and resp!="6" and resp!="5"):
        num_1=float(input("numero 1: "))
        num_2=float(input("numero 2: "))
    if(resp=="1"):
        total=num_1+num_2
    elif(resp=="2"):
        total=num_1-num_2
    elif(resp=="3"):
        total=num_1*num_2
    elif(resp=="4"):
        total=num_1/num_2
    elif(resp=="5"):
        saludo()
    elif(resp=="6"):
        raiz_cuadrada()
    if(resp!="7" and resp!="6" and resp!="5"):
        print(f"es igual a:{total}")
        print(f"\033[92mel total es \033[94m{total}\033[0m")