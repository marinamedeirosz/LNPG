#include <stdio.h>
#include <string.h>

typedef struct
{
    char tipo[7];
    char cor[7];
    int posicao[2];
} Peca;

void inicializar(Peca *p, char tipo[7], char cor[7], int posicao[2])
{
    strncpy(p->tipo, tipo, sizeof(p->tipo) - 1);
    p->tipo[sizeof(p->tipo) - 1] = '\0';
    strncpy(p->tipo, tipo, sizeof(p->tipo) - 1);
    p->tipo[sizeof(p->tipo) - 1] = '\0';
    p->posicao[0] = posicao[0];
    p->posicao[1] = posicao[1];
}
void mover(Peca *p, int pos[2])
{
    p->posicao[0] = pos[0];
    p->posicao[1] = pos[1];
}
void capturar(Peca *p)
{
    p->posicao[0] = 0;
    p->posicao[1] = 0;
}
int verificarMovimento(Peca *p, int pos[2], char type[7])
{
    int linha = p->posicao[0];
    int coluna = p->posicao[1];
    int linhaNova = pos[0];
    int colunaNova = pos[1];
    int difLinha = linha - linhaNova;
    int difColuna = coluna - colunaNova;

    if (strcmp(type, "rei") == 0)
    {
        return (difLinha <= 1 && difColuna <= 1);
    }
    else if (strcmp(type, "rainha") == 0)
    {
        return (linha == linhaNova || coluna == colunaNova || difLinha == difColuna);
    }
    else if (strcmp(type, "torre") == 0)
    {
        return (linha == linhaNova || coluna == colunaNova);
    }
    else if (strcmp(type, "bispo") == 0)
    {
        return (difLinha == difColuna);
    }
    else if (strcmp(type, "cavalo") == 0)
    {
        return ((difLinha == 2 && difColuna == 1) || (difLinha == 1 && difColuna == 2));
    }
    else if (strcmp(type, "peao") == 0)
    {
        return (coluna == colunaNova && difLinha == 1);
    }
    else
    {
        return 0;
    }
}
char *getTipo(Peca *p)
{
    return p->tipo;
}
char *getCor(Peca *p)
{
    return p->cor;
}
int *getPosicao(Peca *p)
{
    return p->posicao;
}