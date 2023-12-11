def listarAlbuns():
    albuns = []
    with open("dados.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo.readlines():
            info = linha.strip().split("|")
            albuns.append(info)
    return albuns