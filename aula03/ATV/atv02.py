# A Secretaría de Meio Ambiente, que controla o índice de poluição, 
# mantém três grupos de indústrias que são altamente poluentes do 
# meio ambiente. A tabela a seguir indica a ação a ser tomada pela 
# Secretaria de acordo com o índice de poluição, leia o índice de 
# poluição:

indice_poluicao = input("Digite o Índice de Poluição: ")

match indice_poluicao:
    case 0 | 1 | 2:
        print("Seu indice de poluição está aceitavel")
    case 3 | 4 | 5:
        print("Você tem que suspender as atividade do Grupo 1")
    case 6 | 7:
        print("Você tem que suspender as atividade do Grupo 1 e Grupo 2")
    case _:
        print("Suspender atividades de todos os grupos!!")