salario = int(input("Digite seu salario atual: "))
perc = int(input("Digite o percentual de reajuste: "))

calc = (perc * salario)/ 100
calc2 = salario + calc

print(f"Seu salario reajustado é de R${calc2}")