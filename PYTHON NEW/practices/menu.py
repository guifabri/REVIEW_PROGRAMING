def odd_even(x):
    return x % 2 == 0
def tiene_raiz(a):
    return (a**(1/2)%1==0)
def es_primo(c):
    cont = 0
    for i in range(1,c+1,1):
        if(c/i % 1 == 0):
            cont+=1
        if(cont==2 and i!=c):
            return False
    return cont ==2
resp=""
while(resp!="0"):
    print("MENU")
    print("1.Par/impar")
    print("2.Es primo ")
    print("3.Tiene raiz cuadrada")
    print("0.Salida\n")
    resp=input("Escoge una opcion: ")
    if(resp=="1"):
        x= int(input("Ingresa el numero: "))
        if(odd_even(x)):
            print(f"El numero es par")
        else:
            print("El numero es impar")
    elif (resp=="3"):
        num = int(input("Ingrese un numero a evaluar: "))
        if(not tiene_raiz(num)):
            print("El numero no es un cuadrado perfecto")
        else:
            print("El numero es un cuadrado perfecto")
    elif (resp =="2"):
        x = int(input("Ingrese el numero: "))
        if(es_primo(x)):
            print(f"El numero {x} es un numero primo")
        else:
            print("NO es un numero primo")