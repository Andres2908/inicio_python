print("*******************************************************")
print("*Programa que determina el si un número es par o inpar*")
print("*******************************************************")
rep=1
while rep==1:
    
    numero=int(input("Por favor introduce un número entero: "))
    if(numero%2 == 0):
        print("***El número ",numero," es par***\n")
    elif(numero%2 != 0):
        print("***El número ",numero," es impar***\n")
        
    rep=int(input("¿Deseas probar otro número?\nSI[1] \nNO[0]"))
    
          
