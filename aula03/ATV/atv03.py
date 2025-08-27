opcao = int(input("\n 1- Tensão \n 2- Resistência \n 3- Corrente \n 4- Exit \n Escolha a opção: "))

match opcao:
    case 1:
        float(input("Digite a quantidade em Tensão: "))