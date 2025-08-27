num1 = int(input("Digite um número inteiro: "))

if num1 % 2 == 0:
    calc1 = num1 ** 2
    print(f"Seu numero é par e ao quadrado é {calc1}")
else:
    calc2 = num1 ** 3
    print(f"Seu numero é impar e ao cubo é {calc2}")