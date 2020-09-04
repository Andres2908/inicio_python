print("Bienvenido al sistema escolar para calcular el promedio del alumno")
nombre=str(input("Cuál es el nombre del estudiante: "))

promedio = float(input(nombre+" cuál es tu calificación de matemáticas ? "))
promedio += float(input(nombre+" cuál es tu calificación de química ? "))
promedio += float(input(nombre+" cuál es tu calificación de biología ? "))
promedio /= 3

if promedio >= 6 :
    print("Felicidades "+nombre+" aprobaste con un promedio de :",round(promedio,2))
else :
    print(nombre+" tu calificación no es suficiente para aprobar")
    print("Tu promedio es: ",round(promedio,2))
