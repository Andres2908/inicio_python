print("*******************")
print("*Número mas grande*")
print("*******************")
rep=1

while rep==1:
    num1=int(input("Dígita el primero número: "))
    num2=int(input("Dígita el segundo número: "))
    num3=int(input("Dígita el tercero número: "))

    if num1>num2:
        if num1>num3:
            print("El número ",num1," es el mas grande de los tres")

    elif num2>num3:
        if num2>num3:
            print("El número ",num2," es el mas grande de los tres")

    elif num3>num1:
        if num3>num2:
            print("El número ",num3," es el mas grande de los tres")

    rep=int(input("\n¿Quieres probar con otros números? \nSI[1]\nNO[0]"))
