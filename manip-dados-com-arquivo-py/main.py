import re


def validaTelefone(telefone):
    padraoTelefone = re.compile(r'^\d{2} \d{5}-\d{4}$')
    return bool(padraoTelefone.match(telefone))


def escreveDados(nome, idade, sexo, telefone):
    with open("dados.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}|{idade}|{sexo}|{telefone}\n")
    
    
def pedeDados():
    while True:
        nome = input("Digite seu nome (0 para sair): ")
        if nome == "0":
            break
        #valida idade
        while True:
            idade = int(input("Digite sua idade: "))
            if idade <= 0:
                print("Idade inválida")
            else:
                break
        #valida sexo
        while True:
            sexo = input("Digite seu sexo (M/F/O): ")
            if sexo != "M" and sexo != "F" and sexo != "O":
                print("Sexo inválido")
            else:
                break
        #valida telefone
        while True:
            telefone = input("Digite seu telefone (XX XXXXX-XXXX): ")
            if validaTelefone(telefone) == False:
                print("Telefone inválido")
            else:
                break

        escreveDados(nome, idade, sexo, telefone)
        #busca sexo
        while True:
            resposta = input("Deseja pesquisar por sexo? (S/N)")
            if resposta == "S":
                while True:
                    sexoPesquisado = input("Deseja pesquisar M(masculino), F(feminino) ou O(outro)? ")
                    if sexoPesquisado != "M" and sexoPesquisado != "F" and sexoPesquisado != "O":
                        print("Sexo inválido")
                    else:
                        busca_usuario_pelo_sexo(sexoPesquisado)
            elif resposta == "N":
                break
            else:
                print("Resposta inválida")


def imprimeDados():
    with open("dados.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo.readlines():
            listaCont = linha.split("|")
            if listaCont[2] == "M":
                sexo2 = "Masculino"
            elif listaCont[2] == "F":
                sexo2 = "Feminino"
            else:
                sexo2 = "Outro"
            print(f"Nome: {listaCont[0]}")
            print(f"Idade: {listaCont[1]} anos")
            print(f"Sexo: {sexo2}")
            print(f"Telefone: {listaCont[3]}")
        

def busca_usuario_pelo_sexo(sexo):
    with open("dados.txt", "r", encoding="utf-8") as arquivo:
        usuarios = []
        usuariosSelecionados = []
        for linha in arquivo.readlines():
            listaCont = linha.split("|")
            usuarios.append(listaCont)
        for i in usuarios:
            if sexo in i:
                usuariosSelecionados.append(i)
        for j in usuariosSelecionados:
            print(f"Nome: {j[0]}")
            print(f"Idade: {j[1]} anos")
            print(f"Sexo: {j[2]}")
            print(f"Telefone: {j[3]}")


def main():
    pedeDados()
    imprimeDados()
    
    
if __name__ == "__main__":
    main()