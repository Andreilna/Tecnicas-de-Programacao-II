endereco = "Av Clara Gianotti de Souza, 250, Centro, Registro, SP"

end = endereco.split(',')

print(f"Nome da rua é: {end[0]}")
print(f"Número é: {end[1]}")
print(f"O bairro é: {end[2]}")
print(f"A cidade é: {end[3]}")
print(f"O estado é: {end[4]}")