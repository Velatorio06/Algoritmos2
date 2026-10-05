nota = float(input("Introduce tu nota: "))

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

print("Tu categoría es:", categoria)