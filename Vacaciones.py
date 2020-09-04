print("\t\tRAPPI")
print("Binevenido al sistema de vacaciones de rappi")

nombre=str(input("Ingresa tu nombre "))
clave=int(input("Cúal es la clave de tu departamento? "))
años=float(input("Cuántos años levas trabajando en esta empresa? "))

if clave==1 :
    if años<1 :
        print("El trabajador: *"+nombre+"* con clave de departamento: *",clave,"* NO tiene derecho a vacaciones")
    elif años==1 :
        print("El trabajador: *"+nombre+"* con clave de departamento: *",clave,"* tiene derecho a 6 días de vacaciones")
    elif años>=2 and años<=6 :
        print("El trabajador: *"+nombre+"* con clave de departamento: *",clave,"* tiene derecho a 14 días de vacaciones")
    elif años>7 :
        print("El trabajador: *"+nombre+"* con clave de departamento: *",clave,"* tiene derecho a 20 días de vacaciones")
              
if clave==2 :
    if años<1 :
        print("El trabajador: *"+nombre+"* con clave de departamento: *",clave,"* NO tiene derecho a vacaciones")
    elif años==1 :
        print("El trabajador: *"+nombre+"* con clave de departamento: *",clave,"* tiene derecho a 7 días de vacaciones")
    elif años>=2 and años<=6 :
        print("El trabajador: *"+nombre+"* con clave de departamento: *",clave,"* tiene derecho a 15 días de vacaciones")
    elif años>7 :
        print("El trabajador: *"+nombre+"* con clave de departamento: *",clave,"* tiene derecho a 22 días de vacaciones")
  
if clave==1 :
    if años<1 :
        print("El trabajador: *"+nombre+"* con clave de departamento: *",clave,"* NO tiene derecho a vacaciones")
    elif años==1 :
        print("El trabajador: *"+nombre+"* con clave de departamento: *",clave,"* tiene derecho a 10 días de vacaciones")
    elif años>=2 and años<=6 :
        print("El trabajador: *"+nombre+"* con clave de departamento: *",clave,"* tiene derecho a 20 días de vacaciones")
    elif años>7 :
        print("El trabajador: *"+nombre+"* con clave de departamento: *",clave,"* tiene derecho a 30 días de vacaciones")
  
  
