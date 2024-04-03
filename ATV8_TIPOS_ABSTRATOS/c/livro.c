#include <stdio.h>
#include <string.h>

typedef struct
{
    char titulo[50];
    char autor[30];
    int ano;
    int copias;
} Livro;

void inicializar(Livro *l, char titulo[50], char autor[30], int ano, int copias)
{
    strncpy(l->titulo, titulo, sizeof(l->titulo) - 1);
    l->titulo[sizeof(l->titulo) - 1] = '\0';
    strncpy(l->autor, autor, sizeof(l->autor) - 1);
    l->autor[sizeof(l->autor) - 1] = '\0';
    l->ano = ano;
    l->copias = copias;
}
void emprestaCopia(Livro *l)
{
    if (l->copias > 0)
    {
        l->copias--;
    }
}
void devolveCopia(Livro *l)
{
    l->copias++;
}
int verificaCopia(Livro *l)
{
    return l->copias;
}
char *getTitulo(Livro *l)
{
    return l->titulo;
}
char *getAutor(Livro *l)
{
    return l->autor;
}
int getAno(Livro *l)
{
    return l->ano;
}