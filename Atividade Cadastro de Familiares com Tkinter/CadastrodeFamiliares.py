from tkinter import *

def cadastrar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    telefone = entry_telefone.get()
    parentesco = entry_parentesco.get()
    altura = entry_altura.get()

    if nome and idade and telefone and parentesco:
        try:
            idade_int = int(idade)
            maioridade = "Maior de idade" if idade_int >= 18 else "Menor de idade"
            pode_votar = "Pode votar" if idade_int >= 16 else "Não pode votar"
        except ValueError:
            idade_int = 0
            maioridade = "Idade inválida"
            pode_votar = ""

        resultado["text"] += f"\n{nome} | {idade} anos | {telefone} | {parentesco} | {altura} | {maioridade} | {pode_votar}"

        entry_nome.delete(0, END)
        entry_idade.delete(0, END)
        entry_telefone.delete(0, END)
        entry_parentesco.delete(0, END)
        entry_altura.delete(0, END)

tela = Tk()
tela.title("Cadastro de Familiares")
tela.configure(background="#e4e4e4")
tela.geometry("500x400")
tela.resizable(True, True)
tela.maxsize(width=800, height=600)
tela.minsize(width=500, height=400)

Label(tela, text="Nome:").place(x=20, y=20)
entry_nome = Entry(tela, width=30)
entry_nome.place(x=150, y=20)

Label(tela, text="Idade:").place(x=20, y=60)
entry_idade = Entry(tela, width=30)
entry_idade.place(x=150, y=60)

Label(tela, text="Telefone:").place(x=20, y=100)
entry_telefone = Entry(tela, width=30)
entry_telefone.place(x=150, y=100)

Label(tela, text="Parentesco:").place(x=20, y=140)
entry_parentesco = Entry(tela, width=30)
entry_parentesco.place(x=150, y=140)

Label(tela, text="Altura:").place(x=20, y=180)
entry_altura = Entry(tela, width=30)
entry_altura.place(x=150, y=180)

btn_botao = Button(tela, text="Cadastrar", command=cadastrar).place(x=200, y=220)

resultado = Label(tela, text="Familiares cadastrados:", justify="left", anchor="w")
resultado.place(x=20, y=260)

resultado["text"] += "\nValdomiro Rodrigues | 53 anos | 13 99999-9999 | Pai | 1.85m | Maior de idade | Pode votar"
resultado["text"] += "\nEdjane Neves | 48 anos | 13 99888-8888 | Mãe | 1.70m | Maior de idade | Pode votar"
resultado["text"] += "\nMaicon Lucas | 28 anos | 13 99777-7777 | Irmão | 1.94m | Maior de idade | Pode votar"
resultado["text"] += "\nMarcos Paulo | 93 anos | 13 99666-6666 | Avô | 1.86m | Maior de idade | Pode votar"

tela.mainloop()