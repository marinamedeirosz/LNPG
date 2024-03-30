#include <stdio.h>
#include <string.h>

typedef struct Peca{
    char *tipo;
    char *cor;
    int[] posicao;
};

void inicializar(Peca *p, char[] tipo, char[] cor, int[] posicao) {
    p->tipo = tipo;
    p->cor = cor;
    p->posicao = posicao;
}
void mover(Peca *p, int[] pos) {
    p->posicao[0] = pos[0];
    p->posicao[1] = pos[1];
}
void capturar(Peca *p) {
   p->posicao[0] = 0;
    p->posicao[1] = 0;
}
int verificarMovimento(Peca *p, int[] pos, char[] type) {
    int linha = p->posicao[0];
    int coluna = p->posicao[1];
    int linhaNova = pos[0];
    int colunaNova = pos[1];
    int difLinha = linha - linhaNova;
    int difColuna = coluna - colunaNova;

    if (strcmp(type, "rei") == 0) {
        return (difLinha <= 1 && difColuna <= 1);
    } else if (strcmp(type, "rainha") == 0) {
        return (linha == linhaNova || coluna == colunaNova || difLinha == difColuna);
    } else if (strcmp(type, "torre") == 0) {
        return (linha == linhaNova || coluna == colunaNova);
    } else if (strcmp(type, "bispo") == 0) {
        return (difLinha == difColuna);
    } else if (strcmp(type, "cavalo") == 0) {
        return ((difLinha == 2 && difColuna == 1) || (difLinha == 1 && difColuna == 2));
    } else if (strcmp(type, "peao") == 0) {
        return (coluna == colunaNova && difLinha == 1);
    } else {
        return 0;
    }
}

char[] getPeca(Peca *p) {
    return p;
}