import db


def getAlbuns():
    return db.listarAlbuns()

def salvaDados(fldnome,spbxano,fldbanda, fldlanc):
    #inicia valores
    nome = str(fldnome.get())
    ano = int(spbxano.get())
    banda = str(fldbanda.get())
    lanc = str(fldlanc.get())

    #salva no txt
    db.escreveDados(nome,ano,banda,lanc) 
             
    #reinicia caixas de texto
    fldnome.delete(0, 'end')
    fldbanda.delete(0, 'end')
    
def buscaAlbumPorArtista(txtfld, tree):
    #inicia valores
    artista = txtfld.get().lower()
    albuns = getAlbuns()
    albunsFiltrados = []

    #reinicia tree
    for item in tree.get_children():
        tree.delete(item)

    #filtra albuns
    for album in albuns:
        print(album)
        if artista in album[2].lower():
            albunsFiltrados.append(album)
            
    return albunsFiltrados
        
def buscaAlbumPorAno(spbx,radio,tree):
    #inicia valores
    ano = spbx.get()
    epoca = radio.get()
    albuns = getAlbuns()
    albunsFiltrados = []
    
    #reinicia tree
    for item in tree.get_children():
        tree.delete(item)
    
    #filtra albuns
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
            
    return albunsFiltrados