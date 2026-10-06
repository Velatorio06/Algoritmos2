def categoria_nota(nota):

    if nota >= 9:
        categoria = "Sobresaliente"
    elif nota >= 7:
        categoria = "Notable"
    elif nota >= 6:
        categoria = "Bien"
    elif nota >= 5:
        categoria = "Suficiente"
    elif nota >= 3:
        categoria = "Suspenso alto"
    else:
        categoria = "Suspenso bajo"

    return categoria


nota = float(input("Introduce tu nota: "))

resultado = categoria_nota(nota)

print("Tu categoría es:", resultado)