numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1== numero2 or numero2 == numero3 or numero1 ==numero3:
    exit() #encerra o programa
if numero1 > numero2 and numero1 > numero3:
    print("O primeiro número é o maior")
if numero2 > numero1 and numero2 > numero3:
    print("O segundo número é o maior")
if numero3 > numero1 and numero3 > numero2:
    print("O terceiro número é maior")