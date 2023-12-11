import domain
from tkinter import *
from tkinter import ttk
import datetime


ano_atual = datetime.datetime.now().year

def salvarDados():
    nome = str(txtfldNome.get())
    ano = int(spbxAno.get())
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
    txtfldBanda.delete(0, 'end')


def buscaAlbumPorArtista(txtfld, tree):
    artista = txtfld.get().lower()
    albuns = domain.getAlbuns()
    albunsFiltrados = []
    
    for item in tree.get_children():
        tree.delete(item)
    
    for album in albuns:
        print(album)
        if artista in album[2].lower():
            albunsFiltrados.append(album)
            
    for album in albunsFiltrados:
        tree.insert("", END, values=album)
            

def janelaMostrarDados():
    winInfo = Toplevel()
    winInfo.title('Musicas registradas')
    width= winInfo.winfo_screenwidth()               
    height= winInfo.winfo_screenheight()               
    winInfo.geometry("%dx%d" % (width, height))
    
    columns = ('Album', 'Cantor', 'Ano', 'Lancamento?')
    
    tree = ttk.Treeview(winInfo, columns=columns, show='headings')
    
    tree.heading('Album', text='Album')
    tree.heading('Cantor', text='Cantor')
    tree.heading('Ano', text='Ano')
    tree.heading('Lancamento?', text='Lancamento?')
    
    albuns = domain.getAlbuns()
    for album in albuns:
        tree.insert("", END, values=album)
        
    tree.grid(row=0, column=0, sticky='nsew')
    
    #scrollbar
    scrollbar = ttk.Scrollbar(winInfo, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')
    btnMenu  = Button(winInfo, text = 'Voltar', command=winInfo.destroy)
    btnMenu.grid(row=2, column=1)  


def janelaBuscaArtista():
    winBusca = Toplevel()
    winBusca.title('Musicas registradas')
    width= winBusca.winfo_screenwidth()               
    height= winBusca.winfo_screenheight()               
    winBusca.geometry("%dx%d" % (width, height))
    
    txtfldCantor = Entry(winBusca, text='Banda do album', bd=5, width=45)
    txtfldCantor.grid(row=0, column=0, padx=10, pady=10)
    
    btnBusca = Button(winBusca, text='Buscar', command=lambda: buscaAlbumPorArtista(txtfldCantor, treeBusca))
    btnBusca.grid(row=0, column=1, padx=10, pady=10)
    
    columns = ('Album', 'Cantor', 'Ano', 'Lancamento?')
    treeBusca = ttk.Treeview(winBusca, columns=columns, show='headings')
    treeBusca.heading('Album', text='Album')
    treeBusca.heading('Cantor', text='Cantor')
    treeBusca.heading('Ano', text='Ano')
    treeBusca.heading('Lancamento?', text='Lancamento?')
    treeBusca.grid(row=1, column=0, columnspan=2, sticky='ns', padx=10, pady=10)
    
    #scrollbar
    scrollbar = ttk.Scrollbar(winBusca, orient=VERTICAL, command=treeBusca.yview)
    treeBusca.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=2, sticky='ns', padx=(0, 10))

    
    btnMenu  = Button(winBusca, text = 'Voltar', command=winBusca.destroy)
    btnMenu.grid(row=2, column=0, columnspan=2, pady=10)
    
    
    for i in range(3):
        winBusca.columnconfigure(i, weight=1)
        winBusca.rowconfigure(i, weight=1)
    winBusca.rowconfigure(1, weight=1)

    
#janela de cadastro
winCad = Tk()
winCad.title("Cadastro de musica")
width= winCad.winfo_screenwidth()               
height= winCad.winfo_screenheight()               
winCad.geometry("%dx%d" % (width, height))

#bloco nome do album
lblNome = Label(winCad, text='Nome do album:')
txtfldNome = Entry(winCad, text='Nome do album', bd=5, width=45)
lblNome.place(x=100, y=100)
txtfldNome.place(x=250, y=100)

#bloco ano do album
lblAno = Label(winCad, text='Ano do album:')
spbxAno = Spinbox(winCad, from_='1800', to=ano_atual)
lblAno.place(x=100, y=150)
spbxAno.place(x=250, y=150)

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

#botao lista dados
btnLista = Button(winCad, text='Listar dados', command=janelaMostrarDados)
btnLista.place(x=350, y=300)

#botao busca por artista
btnLista = Button(winCad, text='Pesquisar por artista', command=janelaBuscaArtista)
btnLista.place(x=100, y=300)

winCad.mainloop()