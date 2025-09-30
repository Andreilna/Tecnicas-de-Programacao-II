from tkinter import *
from tkinter import messagebox, filedialog, ttk
import sqlite3
from PIL import Image, ImageTk

# Janela principal
tela = Tk()
tela.title("Gestão de Animais")
var = StringVar()
var.set("m")
largura = 800
altura = 600

# Banco de dados
conn = sqlite3.connect('MyDB.db')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS pessoas(
    codigo INT PRIMARY KEY, 
    nome TEXT, 
    idade TEXT, 
    sexo TEXT, 
    altura TEXT, 
    peso TEXT, 
    cidade TEXT, 
    datanasc TEXT, 
    dataAtual TEXT, 
    dataCadastro TEXT, 
    descricao TEXT
)""")
conn.commit()
conn.close()

# Função escolher imagem
def escolher_imagem():
    caminho_imagem = filedialog.askopenfilename(
        title="Escolha uma imagem",
        filetypes=(("Arquivos de imagem", "*.jpg;*.jpeg;*.png"), ("Todos os arquivos", "*.*"))
    )
    if not caminho_imagem:
        return
    imagem_pil = Image.open(caminho_imagem)
    largura, altura = imagem_pil.size
    if largura > 150:
        proporcao = largura / 150
        nova_altura = int(altura / proporcao)
        imagem_pil = imagem_pil.resize((110, nova_altura))
    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    lbl_imagem = Label(tela, image=imagem_tk)
    lbl_imagem.image = imagem_tk
    lbl_imagem.place(x=10, y=50)

# CRUD
def insercao():
    conn = sqlite3.connect("MyDB.db")
    cur = conn.cursor()

    cur.execute("""INSERT INTO pessoas VALUES 
    (:codigo, :nome, :idade, :sexo, :altura, :peso, :cidade, :datanasc, :dataAtual, :dataCadastro, :descricao)""",
    {
        'codigo': txt_codigo.get(),
        'nome': txt_nome.get(),
        'idade': txt_idade.get(),
        'sexo': var.get(),
        'altura': txt_altura.get(),
        'peso': txt_peso.get(),
        'cidade': txt_cidade.get(),
        'datanasc': txt_data_nascimento.get(),
        'dataAtual': txt_data_atualizacao.get(),
        'dataCadastro': txt_data_cadastro.get(),
        'descricao': txt_descricao.get("1.0", END).strip()
    })

    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Registro inserido!")

def consulta():
    conn = sqlite3.connect("MyDB.db")
    cur = conn.cursor()
    cur.execute('SELECT *, oid FROM pessoas')
    records = cur.fetchall()
    conn.close()

    print_records = ""
    for rec in records:
        print_records += (
            f"Codigo: {rec[0]} Nome: {rec[1]} Idade: {rec[2]} Sexo: {rec[3]}\n"
            f"Altura: {rec[4]} Peso: {rec[5]} Cidade: {rec[6]}\n"
            f"Data Nasc: {rec[7]} Cadastro: {rec[9]} Atualização: {rec[8]}\n"
            f"Descrição: {rec[10]}\n\n"
        )
    Label(tela, text=print_records, justify=LEFT).place(x=20, y=400)

def delete():
    conn = sqlite3.connect("MyDB.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM pessoas WHERE codigo = ?", (txt_codigo.get(),))
    conn.commit()
    conn.close()
    messagebox.showinfo("Excluído", "Registro deletado!")

def update():
    conn = sqlite3.connect("MyDB.db")
    cur = conn.cursor()
    cur.execute("""UPDATE pessoas SET
                nome=:nome, idade=:idade, sexo=:sexo, altura=:altura, peso=:peso,
                cidade=:cidade, datanasc=:datanasc, dataAtual=:dataAtual, 
                dataCadastro=:dataCadastro, descricao=:descricao
                WHERE codigo=:codigo""",
                {
                    'codigo': txt_codigo.get(),
                    'nome': txt_nome.get(),
                    'idade': txt_idade.get(),
                    'sexo': var.get(),
                    'altura': txt_altura.get(),
                    'peso': txt_peso.get(),
                    'cidade': txt_cidade.get(),
                    'datanasc': txt_data_nascimento.get(),
                    'dataAtual': txt_data_atualizacao.get(),
                    'dataCadastro': txt_data_cadastro.get(),
                    'descricao': txt_descricao.get("1.0", END).strip()
                })
    conn.commit()
    conn.close()
    messagebox.showinfo("Atualizado", "Registro alterado!")

# Widgets
btn_escolher = Button(tela, text="Escolher imagem", command=escolher_imagem)
btn_escolher.place(x=10, y=140)

lbl_codigo = Label(tela, text="Código:").place(x=130, y=50)
lbl_nome = Label(tela, text="Nome:").place(x=130, y=80)
lbl_idade = Label(tela, text="Idade:").place(x=510, y=80)
lbl_sexo = Label(tela, text="Sexo:").place(x=130, y=110)
lbl_altura = Label(tela, text="Altura:").place(x=260, y=110)
lbl_peso = Label(tela, text="Peso:").place(x=380, y=110)
lbl_cidade = Label(tela, text="Cidade:").place(x=510, y=110)
lbl_data_nascimento = Label(tela, text="Data Nascimento:").place(x=130, y=140)
lbl_data_atualizacao = Label(tela, text="Data Atualização:").place(x=130, y=170)
lbl_data_cadastro = Label(tela, text="Data Cadastro:").place(x=380, y=140)
lbl_descricao = Label(tela, text="Descrição:").place(x=130, y=200)

txt_codigo = Entry(tela, width=10)
txt_nome = Entry(tela, width=50)
txt_idade = Entry(tela, width=20)
txt_altura = Entry(tela, width=10)
txt_peso = Entry(tela, width=10)
txt_cidade = ttk.Combobox(tela, values=["Basset Hound", "Beagle", "Bichon Frisé"], width=10)
txt_data_nascimento = Entry(tela, width=20)
txt_data_atualizacao = Entry(tela, width=20)
txt_data_cadastro = Entry(tela, width=20)
txt_descricao = Text(tela, width=50, height=5)

txt_codigo.place(x=180, y=50)
txt_nome.place(x=180, y=80)
txt_idade.place(x=560, y=80)
txt_altura.place(x=300, y=110)
txt_peso.place(x=420, y=110)
txt_cidade.place(x=560, y=110)
txt_data_nascimento.place(x=240, y=140)
txt_data_atualizacao.place(x=240, y=170)
txt_data_cadastro.place(x=470, y=140)
txt_descricao.place(x=190, y=205)

rdb_buttonm = Radiobutton(tela, text="M", variable=var, value="m").place(x=180, y=110)
rdb_buttonf = Radiobutton(tela, text="F", variable=var, value="f").place(x=220, y=110)

# Botões CRUD
Button(tela, text="Salvar", command=insercao).place(x=130, y=350)
Button(tela, text="Excluir", command=delete).place(x=200, y=350)
Button(tela, text="Alterar", command=update).place(x=270, y=350)
Button(tela, text="Consultar", command=consulta).place(x=340, y=350)
Button(tela, text="Sair", command=tela.quit).place(x=620, y=350)

# Centralizar tela
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

tela.mainloop()