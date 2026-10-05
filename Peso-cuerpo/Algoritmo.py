peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Normal"
else:
    categoria = "Obeso"

print("Tu IMC es:", imc)
print("Tu categoría es:", categoria)
