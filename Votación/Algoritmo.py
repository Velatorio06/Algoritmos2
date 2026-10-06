def acceso_voto(edad):

    if edad >= 18:
        puede_votar = "Puedes votar"
    else:
        puede_votar = "No puedes votar"

    return puede_votar


edad = int(input("Introduce tu edad: "))
resultado = acceso_voto(edad)
print(resultado)