# valor = [10, 20, 30, 40]
# print(valor)

tamanho = int(input("Digite o tamanho do vetor: "))

vetor = []

for i in range(tamanho):
    elemento = int(input(f"Digite o elemento {i + 1} do vetor: "))
    vetor.append(elemento)
    
print("Vetor:", vetor)
