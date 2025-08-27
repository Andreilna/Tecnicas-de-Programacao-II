branco = int(input("Digite a quantidade de votos brancos: "))
nulo = int(input("Digite a quantidade de votos nulos: "))
valido = int(input("Digite a quantidade de votos válidos: "))

total = branco + nulo + valido

percbrancos = (branco * 100)/ total
percnulos = (nulo * 100)/ total
percvalidos = (valido * 100)/ total

print(f"\nPercentual Brancos: {percbrancos:.2f}%")
print(f"Percentual Nulos: {percnulos:.2f}%")
print(f"Percentual Validos: {percvalidos:.2f}%\n")