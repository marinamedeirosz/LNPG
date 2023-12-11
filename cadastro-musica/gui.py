import domain
from tkinter import *
from tkinter import ttk
import datetime


ano_atual = datetime.datetime.now().year


def incluiDadosFiltradosAno(spbx,ano,tree):
    albunsFiltrados = domain.buscaAlbumPorAno(spbx, ano, tree)
    for album in albunsFiltrados:
        tree.insert("", END, values=album)
        

def incluiDadosFiltradosArtista(cantor,tree):
    albunsFiltrados = domain.buscaAlbumPorArtista(cantor,tree)
    for album in albunsFiltrados:
        tree.insert("", END, values=album)


def janelaMostrarDados():
    #cria janela
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
    tree.grid(row=1, column=0, columnspan=2, sticky='ns', padx=10, pady=10)
    
    #scrollbar
    scrollbar = ttk.Scrollbar(winInfo, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=2, sticky='ns', padx=(0, 10))
    
    #botao voltar
    btnMenu  = Button(winInfo, text = 'Voltar', command=winInfo.destroy)
    btnMenu.grid(row=2, column=1)  


def janelaBuscaArtista():
    #cria janela de busca por artista
    winBusca = Toplevel()
    winBusca.title('Musicas registradas')
    width= winBusca.winfo_screenwidth()               
    height= winBusca.winfo_screenheight()               
    winBusca.geometry("%dx%d" % (width, height))
    
    #bloco cantor pesquisado
    txtfldCantor = Entry(winBusca, text='Banda do album', bd=5, width=45)
    txtfldCantor.grid(row=0, column=0, padx=10, pady=10)
    
    #botao buscar
    btnBusca = Button(winBusca, text='Buscar', command=lambda: incluiDadosFiltradosArtista(txtfldCantor, treeBusca))
    btnBusca.grid(row=0, column=1, padx=10, pady=10)
    
    #tree
    columns = ('Album', 'Cantor', 'Ano', 'Lancamento?')
    treeBusca = ttk.Treeview(winBusca, columns=columns, show='headings')
    for col in columns:
        treeBusca.heading(col, text=col)
    treeBusca.grid(row=1, column=0, columnspan=2, sticky='ns', padx=10, pady=10)
    
    #scrollbar
    scrollbar = ttk.Scrollbar(winBusca, orient=VERTICAL, command=treeBusca.yview)
    treeBusca.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=2, sticky='ns', padx=(0, 10))
    
    #botao voltar
    btnMenu  = Button(winBusca, text = 'Voltar', command=winBusca.destroy)
    btnMenu.grid(row=2, column=0, columnspan=2, pady=10)
    
    #config columns
    for i in range(3):
        winBusca.columnconfigure(i, weight=1)
        winBusca.rowconfigure(i, weight=1)
    winBusca.rowconfigure(1, weight=1)


def janelaBuscaAno():
    #cria janela de busca por ano
    winBuscaAno = Toplevel()
    winBuscaAno.title('Busca por Ano')
    width= winBuscaAno.winfo_screenwidth()               
    height= winBuscaAno.winfo_screenheight()               
    winBuscaAno.geometry("%dx%d" % (width, height))
    
    #bloco ano busca
    lblAnoBusca = Label(winBuscaAno, text='Ano do album:')
    spbxAnoBusca = Spinbox(winBuscaAno, from_='1800', to=ano_atual)
    lblAnoBusca.grid(row=0,column=0,padx=10,pady=10)
    spbxAnoBusca.grid(row=0,column=1,padx=10,pady=10)
    
    #radio ano
    ano = StringVar()
    ano.set("Anterior")
    
    rdoAnterior=Radiobutton(winBuscaAno,text='Anterior a', variable=ano, value='Anterior')
    rdoAnterior.grid(row=1, column=0, padx=5, pady=5)
    rdoIgual=Radiobutton(winBuscaAno,text='Igual a ', variable=ano, value='Igual')
    rdoIgual.grid(row=1, column=1, padx=5, pady=5)
    rdoDepois=Radiobutton(winBuscaAno,text='Depois de ', variable=ano, value='Depois')
    rdoDepois.grid(row=1, column=2, padx=5, pady=5)
    
    #botao buscar
    btnBuscaAno = Button(winBuscaAno,text='Buscar',command=lambda: incluiDadosFiltradosAno(spbxAnoBusca,ano, treeBuscaAno ))
    btnBuscaAno.grid(row=2, column=0, columnspan=3, pady=10)
    
    #tree
    columns = ('Album', 'Cantor', 'Ano', 'Lancamento?')
    treeBuscaAno = ttk.Treeview(winBuscaAno, columns=columns, show='headings')
    for col in columns:
        treeBuscaAno.heading(col, text=col)
    treeBuscaAno.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='ns')
    
    #scrollbar
    scrollbar = Scrollbar(winBuscaAno, orient=VERTICAL, command=treeBuscaAno.yview)
    treeBuscaAno.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=3, column=3, sticky='ns', padx=(0,10))

    #botao voltar
    btnMenu  = Button(winBuscaAno, text = 'Voltar', command=winBuscaAno.destroy)
    btnMenu.grid(row=4, column=0, columnspan=2, pady=10)
    
    #config columns
    for i in range(5):
        winBuscaAno.columnconfigure(i, weight=1)
        winBuscaAno.rowconfigure(i, weight=1)
    winBuscaAno.rowconfigure(1, weight=1)
    
    
def janelaCadastro():
    #janela de cadastro
    winCad = Tk()
    winCad.title("Cadastro de musica")
    width= winCad.winfo_screenwidth()               
    height= winCad.winfo_screenheight()               
    winCad.geometry("%dx%d" % (width, height))
            
    #bloco nome do album
    lblNome = Label(winCad, text='Nome do album:')
    txtfldNome = Entry(winCad, text='Nome do album', bd=5, width=45)
    lblNome.grid(row=0, column=0, padx=10, pady=10, sticky='e')
    txtfldNome.grid(row=0, column=1, padx=10, pady=10,sticky='w')

    #bloco ano do album
    lblAno = Label(winCad, text='Ano do album:')
    spbxAno = Spinbox(winCad, from_='1800', to=ano_atual)
    lblAno.grid(row=1, column=0, padx=10, pady=10,sticky='e')
    spbxAno.grid(row=1, column=1, padx=10, pady=10,sticky='w')

    #bloco banda do album
    lblBanda = Label(winCad, text='Banda do album:')
    txtfldBanda = Entry(winCad, text='Banda do album', bd=5, width=45)
    lblBanda.grid(row=2, column=0, padx=10, pady=10,sticky='e')
    txtfldBanda.grid(row=2, column=1, padx=10, pady=10,sticky='w')

    #bloco lancamento do album
    lblLanc = Label(winCad, text='Album lançamento?')
    lblLanc.grid(row=3, column=0, padx=10, pady=10, sticky='e')
    v0 = StringVar()
    v0.set('Sim')
    r1 = Radiobutton(winCad, text='sim', variable = v0, value = 'Sim')
    r2  = Radiobutton(winCad, text='nao', variable = v0, value = 'Nao')
    r1.grid(row=3, column=1, padx=10, pady=10,sticky='w')
    r2.grid(row=3, column=2, padx=10, pady=10,sticky='w')

    #botao busca por artista
    btnBuscaArtista = Button(winCad, text='Pesquisar por artista', command=janelaBuscaArtista)
    btnBuscaArtista.grid(row=4, column=0, columnspan=2, padx=10, pady=10,sticky='nsew')

    #botao envia dados
    btnSubmit = Button(winCad, text='Salvar', command=lambda: domain.salvaDados(txtfldNome, spbxAno, txtfldBanda, v0))
    btnSubmit.grid(row=4, column=2, padx=10, pady=10,sticky='nsew')

    #botao lista dados
    btnLista = Button(winCad, text='Listar dados', command=janelaMostrarDados)
    btnLista.grid(row=4, column=3, padx=10, pady=10,sticky='nsew')

    #botao busca por ano
    btnBuscaAno = Button(winCad, text='Pesquisar por ano', command=janelaBuscaAno)
    btnBuscaAno.grid(row=4, column=4, padx=10, pady=10,sticky='nsew')
    
    return winCad


if __name__ == "__main__":
    win = janelaCadastro()
    win.mainloop()