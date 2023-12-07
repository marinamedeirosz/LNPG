from tkinter import *


def salvarDados():
    nome = str(txtfldNome.get())
    ano = int(txtfldAno.get())
    banda = str(txtfldBanda.get())
    lanc = int(v0.get())
    if lanc == 1:
        lanc = 'sim'
    else:
        lanc = 'nao'
        
    with open("dados.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}|{ano}|{banda}|{lanc}\n")
    
    #reinicia caixas de texto
    txtfldNome.delete(0, 'end')
    txtfldAno.delete(0, 'end')
    txtfldBanda.delete(0, 'end')
        

def listarDados():
    #esquece botao
    btnLista.place_forget()
    
    with open("dados.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo.readlines():
            listaCont = linha.split("|")
            lblN = Label(winInfo, text = f"Nome: {listaCont[0]}")
            lblA = Label(winInfo, text = f"Ano: {listaCont[1]}")
            lblB = Label(winInfo, text = f"Banda: {listaCont[2]}")
            lblL = Label(winInfo, text = f"Lançamento? {listaCont[3]}")
            lblN.pack()
            lblA.pack()
            lblB.pack()
            lblL.pack()

#janela de cadastro
winCad = Toplevel()
winCad.title("Cadastro de musica")
winCad.geometry('600x400')

#bloco nome do album
lblNome = Label(winCad, text='Nome do album:')
txtfldNome = Entry(winCad, text='Nome do album', bd=5, width=45)
lblNome.place(x=100, y=100)
txtfldNome.place(x=250, y=100)

#bloco ano do album
lblAno = Label(winCad, text='Ano do album:')
txtfldAno = Entry(winCad, text='Ano do album', bd=5, width=45)
lblAno.place(x=100, y=150)
txtfldAno.place(x=250, y=150)

#bloco banda do album
lblBanda = Label(winCad, text='Banda do album:')
txtfldBanda = Entry(winCad, text='Banda do album', bd=5, width=45)
lblBanda.place(x=100, y=200)
txtfldBanda.place(x=250, y=200)

#bloco lancamento do album
lblLanc = Label(winCad, text='Album lançamento?')
lblLanc.place(x=100, y=250)
v0 = IntVar()
v0.set(1)
r1 = Radiobutton(winCad, text='sim', variable = v0, value = 1)
r2  = Radiobutton(winCad, text='nao', variable = v0, value = 2)
r1.place(x=250, y=250)
r2.place(x=350, y=250)

#botao envia dados
btnSubmit = Button(winCad, text='Salvar', command=salvarDados)
btnSubmit.place(x=250, y=300)


#janela mostra dados
winInfo = Tk()
winInfo.title('Musicas registradas')
winInfo.geometry('')

#botao lista dados
btnLista = Button(winInfo, text='Listar dados', command=listarDados)
btnLista.place(x=5, y=5)

winCad.mainloop()