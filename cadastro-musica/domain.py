import db

def getAlbuns():
    return db.listarAlbuns()

def salvaDados(fldnome,spbxano,fldbanda, fldlanc):
    #pega valores
    nome = str(fldnome.get())
    ano = int(spbxano.get())
    banda = str(fldbanda.get())
    lanc = str(fldlanc.get())

    #salva no txt
    db.escreveDados(nome,ano,banda,lanc) 
             
    #reinicia caixas de texto
    fldnome.delete(0, 'end')
    fldbanda.delete(0, 'end')