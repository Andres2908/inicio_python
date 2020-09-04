print("***CONVERSOR***\n")

print("Menu de opciones\n")

print("Presiona 1 para convertir de número a palabra")
print("presiona 2 para convertir de palabra a numero\n")

opcion=int(input("¿Cúal es la opción deseada? "))

if opcion==1 :
    numero=int(input("¿Cúal es el número qué deseas convertir a palabra? "))
    if numero==1 :
        print("El número registrado es: **UNO** ")
    elif numero==2 :
        print("El número registrado es: **DOS** ")
    elif numero==3 :
        print("El número registrado es: **TRES** ")
    else :
        print("El número no existe en la base de datos")

if opcion==2 :
    palabra=str(input("Cúal es la palabra qué deseas convertir a número? "))
    if palabra=="uno" :
        print("El número registrado es: **1** ")
    elif palabra=="dos" :
        print("El número registrado es: **2** ")
    elif palabra=="tres" :
        print("El número registrado es: **3** ")
    else :
        print("El número no existe en la base de datos")
