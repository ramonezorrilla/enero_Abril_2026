print("¡Hola! Soy un robot que recomienda películas ")

estado = input("¿Cómo te sientes hoy? (feliz/triste): ")

if estado == "feliz":
    accion = input("¿Te gustan las películas de acción? (si/no): ")
    if accion == "si":
        print("Te recomiendo: Avengers ")
    else:
        print("Te recomiendo: Toy Story ")

elif estado == "triste":
    tipo = input("¿Prefieres comedia o drama?: ")
    if tipo == "comedia":
        print("Te recomiendo: The Mask ")
    else:
        print("Te recomiendo: Forrest Gump ")

else:
    print("No entendí tu respuesta ")