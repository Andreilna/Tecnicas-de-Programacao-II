altura = int(input("Digite a altura da parede em metros: "))
largura = int(input("Digite a largura da parede em metros: "))
alturaAzu = float(input("Digite a altura do azulejo em cm: "))
larguraAzu = float(input("Digite a largura do azulejo em cm: "))

calcParede = altura * largura

calcAzulejo = alturaAzu * larguraAzu
calcMetroAzu = calcAzulejo / 100

calcQuantidade = calcMetroAzu / calcParede

print(f"Com {calcParede} metros de parede, sendo {calcMetroAzu:.2f} cm de azulejo, você precisará de {calcQuantidade} azulejos")