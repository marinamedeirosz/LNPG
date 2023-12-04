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
                
        
def main():
    pedeDados()
    
    
if __name__ == "__main__":
    main()
