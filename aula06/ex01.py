from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

# Criar janela
tela = Tk()
tela.title("Gestão de Animais")
var = StringVar(value="m")

largura = 700
altura = 400
pasta_inicial = ""

# Função escolher imagem
def escolher_imagem():
    caminho_imagem = filedialog.askopenfilename(
        initialdir=pasta_inicial,
        title="Escolha uma imagem",
        filetypes=(("Arquivos de imagem", "*.jpg;*.jpeg;*.png"),
                   ("Todos os arquivos", "*.*"))
    )
    if not caminho_imagem:
        return  # usuário cancelou

    imagem_pil = Image.open(caminho_imagem)
    largura_img, altura_img = imagem_pil.size
    if largura_img > 150:
        proporcao = largura_img / 150
        nova_altura = int(altura_img / proporcao)
        imagem_pil = imagem_pil.resize((150, nova_altura))

    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    lbl_imagem.config(image=imagem_tk)
    lbl_imagem.image = imagem_tk  # manter referência

# Botão escolher imagem
btn_escolher = Button(tela, text="Escolher imagem", command=escolher_imagem)
btn_escolher.place(x=10, y=140)

lbl_imagem = Label(tela)
lbl_imagem.place(x=10, y=50)

# Labels
lbl_codigo = Label(tela, text="Código:").place(x=130, y=50)
lbl_nome = Label(tela, text="Nome:").place(x=130, y=80)
lbl_idade = Label(tela, text="Idade").place(x=510, y=80)
lbl_sexo = Label(tela, text="Sexo").place(x=130, y=110)
lbl_altura = Label(tela, text="Altura").place(x=260, y=110)
lbl_peso = Label(tela, text="Peso").place(x=380, y=110)
lbl_cidade = Label(tela, text="Cidade").place(x=510, y=110)
lbl_data_nascimento = Label(tela, text="Data Nascimento").place(x=130, y=140)
lbl_data_cadastro = Label(tela, text="Data Cadastro").place(x=380, y=140)
lbl_data_atualizacao = Label(tela, text="Data Atualização").place(x=130, y=170)
lbl_descricao = Label(tela, text="Descrição").place(x=130, y=200)

# Entradas
txt_codigo = Entry(tela, width=10)
txt_nome = Entry(tela, width=50)
txt_idade = Entry(tela, width=20)
txt_sexo = Entry(tela, width=10)
txt_altura = Entry(tela, width=10)
txt_peso = Entry(tela, width=10)
txt_cidade = ttk.Combobox(tela, values=["Basset Hound", "Beagle", "Bichon Frisé"], width=10)
txt_data_nascimento = Entry(tela, width=20)
txt_data_cadastro = Entry(tela, width=20)
txt_data_atualizacao = Entry(tela, width=20)
txt_descricao = Text(tela, width=50, height=5)

rdb_buttonm = Radiobutton(tela, text="M", variable=var, value="m")
rdb_buttonf = Radiobutton(tela, text="F", variable=var, value="f")

# Posicionamento
txt_codigo.place(x=180, y=50)
txt_nome.place(x=180, y=80)
txt_idade.place(x=560, y=80)
txt_altura.place(x=300, y=110)
txt_peso.place(x=420, y=110)
txt_cidade.place(x=560, y=110)
txt_data_nascimento.place(x=240, y=140)
txt_data_cadastro.place(x=470, y=140)
txt_data_atualizacao.place(x=240, y=170)
txt_descricao.place(x=190, y=205)

rdb_buttonm.place(x=180, y=110)
rdb_buttonf.place(x=220, y=110)

# Ícones dos botões
foto_salvar = PhotoImage(file=r"icones\salvar.png")
foto_excluir = PhotoImage(file=r"icones\excluir.png")
foto_alterar = PhotoImage(file=r"icones\alterar.png")
foto_consultar = PhotoImage(file=r"icones\consultar.png")
foto_sair = PhotoImage(file=r"icones\sair.png")

btn_salvar = Button(tela, text="Salvar", image=foto_salvar, compound=TOP)
btn_excluir = Button(tela, text="Excluir", image=foto_excluir, compound=TOP)
btn_alterar = Button(tela, text="Alterar", image=foto_alterar, compound=TOP)
btn_consultar = Button(tela, text="Consultar", image=foto_consultar, compound=TOP)
btn_sair = Button(tela, text="Sair", image=foto_sair, compound=RIGHT, command=tela.quit)

btn_salvar.place(x=130, y=310)
btn_excluir.place(x=200, y=310)
btn_alterar.place(x=270, y=310)
btn_consultar.place(x=340, y=310)
btn_sair.place(x=620, y=340)

# Valores padrão
txt_codigo.insert(0, "01")
txt_nome.insert(0, "Maylon")
txt_altura.insert(0, "Não Definido")
txt_peso.insert(0, "3")
txt_idade.insert(0, "29 anos")

# Centralizar tela
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = int(largura_screen/2 - largura/2)
posy = int(altura_screen/2 - altura/2)
tela.geometry(f"{largura}x{altura}+{posx}+{posy}")

tela.mainloop()