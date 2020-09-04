print("********************************************************")
print("HELLO WORD")
print("********************************************************")
print("""HELLO WORD""")
print('HELLO WORD')
print("HELLO WORD") #Diferentes formas de escribir algo en consola
print(type("HELLO WORD")) #Escribe el tipo de dato
print(type(True))
print("Bye "+" HELLO")
print("********************************************************")

#Listas
print("**LISTAS**")
L=[10,20,30,40,50]
L1=["HELLO WORD",10,True] #Se pueden guardar cosas diferentes
L2=[4,'Hello',[1,2,3]]
colors=['red','green','blue']
print(L[2])
print(L1[0])
print(L2[2])
number_list=list((1,2,3,4))
print(number_list)

r=list(range(1,100))#El rango va desde *1* hasta uno antes del *10* 
print(r)
print(colors)
colors.append('violet')#Agrega un elemento a la lista
print(colors)


print("********************************************************")

#Tuplas
print("**TUPLAS**")
T=(1,2,3,4,5) #Esto es una tupla, las tuplas no se pueden cambiar
print(type((10,20,30,40,60)))
print(T)
print("********************************************************")

#Diccionarios(Sirven para agrupar distintos datos con un nombre clave
print('**DICCIONARIOS**')
Dic={
        "Name ":"Ryan",
        "Lastneme ":"Ray",
        "nickname ":"Rayo"
    }
print(Dic)
print(type({
        "Name ":"Ryan",
        "Lastneme ":"Ray",
        "nickname ":"Rayo"
    }))
print("********************************************************")
#Variables
x, libro = 100, "Francesco"
print(x,libro)
#STRINGS
print("**STRINGS**")
myStr = "hello word car"
name = "Andres"
#print(dir(myStr))
print(myStr.upper())#upper escribe toda la cadena en mayúsculas
print(myStr.lower())#lower escribe toda la cadena en minúsculas
print(myStr.swapcase())#swapcase cambia la primer letra de cada palabra
print(myStr.capitalize())#Genera una mayúscula al inicio de la cadena
print(myStr.replace('hello','Bye').upper())
print(myStr.count('l'))#Cuenta cuantas letras hay en una palabra
print(myStr.startswith('hel'))#Comprueba el inicio de la cadena
print(myStr.endswith('rd'))#Comprueba el final de la cadena
print(myStr.split())#Divide una cadena de texto
print(myStr.find('hello'))#Busca la posición de la letra o caracter
print(len(myStr))#Cuenta la longitud de la cadena
print(myStr.isnumeric())
print(myStr.isalpha())
print(myStr[5])
print("My name is: "+name)
print("********************************************************")
age=int(input("Insert your age: "))
print(age+20)
print("********************************************************")

print("********************************************************")

print("********************************************************")
