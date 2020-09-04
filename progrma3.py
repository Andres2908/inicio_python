print("Esto es una busqueda de cadenas")
mensaje="Hola Andres"
nombre="Hola"
buscar=mensaje.find(nombre)
print(buscar)


print("Esto es una extraccion")
nombre = "Andres Saavedra"
buscar1=nombre.find("Andres")
buscar2=nombre.find("Saavedra")
extraer = nombre[buscar1:buscar2]
print(extraer)


print("Esto es una comparacion de cadenas")
nombre1="Andres Saavedra"
nombre2="Diego Saavedra"
extraer1=nombre1[7:14]
extraer2=nombre2[6:13]
if(extraer1==extraer2):
    print("Los ingresados son hermanos")
else:
    print("Los ingresados no son hermanos")

    
    
