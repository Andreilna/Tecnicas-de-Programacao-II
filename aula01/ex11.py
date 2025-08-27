produto = input("Digite o nome de seu produto: ")
qtd = int(input(f"Digite a quantidade de {produto} que foram comprados: "))
valor = float(input(f"Digite o preço de {produto}: "))

calc = qtd * valor

print(f"Comprando {qtd} {produto} no valor de {valor} você gastará: R${calc:.2f}")