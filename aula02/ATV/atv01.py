peso1 = float(input("Digite o peso da pessoa 1: "))
peso2 = float(input("Digite o peso da pessoa 2: "))

if peso1 > peso2:
    print("A pessoa 1 é mais pesada")
elif peso2 > peso1:
    print("A pessoa 2 é mais pesada")
else:
    print("Seus pesos são iguais")