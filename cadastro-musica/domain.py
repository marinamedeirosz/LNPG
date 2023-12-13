import db


def getAlbuns():
    return db.listarAlbuns()


def salvaDados(nome, ano, banda, lanc):
    db.escreveDados(nome, ano, banda, lanc)


def buscaAlbumPorArtista(artista):
    # inicia valores
    albuns = getAlbuns()
    albunsFiltrados = []

    # filtra albuns por artista
    for album in albuns:
        print(album)
        if artista in album[2].lower():
            albunsFiltrados.append(album)

    return albunsFiltrados


def buscaAlbumPorAno(epoca, ano):
    # inicia valores
    albuns = getAlbuns()
    albunsFiltrados = []

    # filtra albuns por epoca
    if epoca == "Anterior":
        for album in albuns:
            if album[1] < ano:
                albunsFiltrados.append(album)
    if epoca == "Igual":
        for album in albuns:
            if album[1] == ano:
                albunsFiltrados.append(album)
    if epoca == "Depois":
        for album in albuns:
            if album[1] > ano:
                albunsFiltrados.append(album)

    return albunsFiltrados
