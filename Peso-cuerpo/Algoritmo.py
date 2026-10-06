def categoria_imc(peso, altura):

    imc = peso / (altura ** 2)

    if imc < 18.5:
        categoria = "Bajo peso"
    elif imc < 25:
        categoria = "Normal"
    else:
        categoria = "Obeso"

    return categoria


peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))

resultado = categoria_imc(peso, altura)

print("Tu categoría es:", resultado)
