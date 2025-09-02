numero = int(input("Digite um tamanho para o vetor: "))

vetor = []

for i in range(numero):
    elemento = int(input(f"Digite o elemento {i + 1} do vetor: "))
    vetor.append(elemento)
    
print("Vetor:", vetor)