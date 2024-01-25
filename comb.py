# Definimos las bases nitrogenadas
bases = ['A', 'C', 'G', 'T']

# Creamos una lista vacía para almacenar todas las combinaciones
combinaciones = []

# Recorremos todas las bases nitrogenadas para generar todas las combinaciones posibles
for base1 in bases:
    for base2 in bases:
        for base3 in bases:
            codon = base1 + base2 + base3
            combinaciones.append(codon)

# Imprimimos todas las combinaciones
print(combinaciones)
