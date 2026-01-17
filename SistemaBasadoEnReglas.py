edad = int(input("Ingrese su edad: "))    
ingresos = float(input("Ingrese sus ingresos mensuales: "))

if edad >= 18 and ingresos >= 30000:
    print("Apto para credito")

elif edad >=18:
    print("Credito Condicionado")

else:
    print("No Apto para credito")
