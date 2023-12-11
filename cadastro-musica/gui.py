import domain
from tkinter import *
from tkinter import ttk
import datetime


ano_atual = datetime.datetime.now().year

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
        
def buscaAlbumPorAno(spbx,radio,tree):
    ano = spbx.get()
    epoca = radio.get()
    albuns = domain.getAlbuns()
    albunsFiltrados = []
    
    for item in tree.get_children():
        tree.delete(item)
        
    if epoca == 'Anterior':
        for album in albuns:
            if album[1] < ano:
                albunsFiltrados.append(album)
    if epoca == 'Igual':
        for album in albuns:
            if album[1] == ano:
                albunsFiltrados.append(album)
    if epoca == 'Depois':
        for album in albuns:
            if album[1] > ano:
                albunsFiltrados.append(album)
            
    for album in albunsFiltrados:
        tree.insert("", END, values=album)
            

def janelaMostrarDados():
    winInfo = Toplevel()
    winInfo.title('Musicas registradas')
    width= winInfo.winfo_screenwidth()               
    height= winInfo.winfo_screenheight()               
    winInfo.geometry("%dx%d" % (width, height))
    
    #tree
    columns = ('Album', 'Cantor', 'Ano', 'Lancamento?')
    tree = ttk.Treeview(winInfo, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)
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
    for col in columns:
        treeBusca.heading(col, text=col)
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


def janelaBuscaAno():
    winBuscaAno = Toplevel()
    winBuscaAno.title('Busca por Ano')
    width= winBuscaAno.winfo_screenwidth()               
    height= winBuscaAno.winfo_screenheight()               
    winBuscaAno.geometry("%dx%d" % (width, height))
    
    lblAnoBusca = Label(winBuscaAno, text='Ano do album:')
    spbxAnoBusca = Spinbox(winBuscaAno, from_='1800', to=ano_atual)
    lblAnoBusca.grid(row=0,column=0,padx=10,pady=10)
    spbxAnoBusca.grid(row=0,column=1,padx=10,pady=10)
    
    ano = StringVar()
    ano.set("Anterior")
    
    rdoAnterior=Radiobutton(winBuscaAno,text='Anterior a', variable=ano, value='Anterior')
    rdoAnterior.grid(row=1, column=0, padx=10, pady=5)
    rdoIgual=Radiobutton(winBuscaAno,text='Igual a ', variable=ano, value='Igual')
    rdoIgual.grid(row=1, column=1, padx=10, pady=5)
    rdoDepois=Radiobutton(winBuscaAno,text='Depois de ', variable=ano, value='Depois')
    rdoDepois.grid(row=1, column=2, padx=10, pady=5)
    
    btnBuscaAno = Button(winBuscaAno,text='Buscar',command=lambda: buscaAlbumPorAno(spbxAnoBusca, ano, treeBuscaAno))
    btnBuscaAno.grid(row=2, column=0, columnspan=3, pady=10)
    
    columns = ('Album', 'Cantor', 'Ano', 'Lancamento?')
    treeBuscaAno = ttk.Treeview(winBuscaAno, columns=columns, show='headings')
    for col in columns:
        treeBuscaAno.heading(col, text=col)
    treeBuscaAno.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')
    
    scrollbar = Scrollbar(winBuscaAno, orient=VERTICAL, command=treeBuscaAno.yview)
    treeBuscaAno.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=3, column=3, sticky='ns')

    for i in range(4):
        winBuscaAno.columnconfigure(i, weight=1)
    winBuscaAno.rowconfigure(3, weight=1)
    

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
v0 = StringVar()
v0.set('Sim')
r1 = Radiobutton(winCad, text='sim', variable = v0, value = 'Sim')
r2  = Radiobutton(winCad, text='nao', variable = v0, value = 'Nao')
r1.place(x=250, y=250)
r2.place(x=350, y=250)

#botao busca por artista
btnLista = Button(winCad, text='Pesquisar por artista', command=janelaBuscaArtista)
btnLista.place(x=100, y=300)

#botao envia dados
btnSubmit = Button(winCad, text='Salvar', command=lambda: domain.salvaDados(txtfldNome, spbxAno, txtfldBanda, v0))
btnSubmit.place(x=250, y=300)

#botao lista dados
btnLista = Button(winCad, text='Listar dados', command=janelaMostrarDados)
btnLista.place(x=350, y=300)

#botao busca por ano
btnLista = Button(winCad, text='Pesquisar por ano', command=janelaBuscaAno)
btnLista.place(x=450, y=300)

winCad.mainloop()