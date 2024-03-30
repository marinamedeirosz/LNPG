#include <stdio.h>

typedef struct Livro{
    char[] titulo;
    char[] autor;
    int ano;
    int copias;
};

void inicializar(Livro *l, char[] titulo, char[] autor, int ano, int copias) {
    l->titulo = titulo;
    l->autor = autor;
    l->ano = ano;
    l->copias = copias;
}
void emprestaCopia(Livro *l) {
    l->copias--;
}
void devolveCopia(Livro *l) {
    l->copias++;
}
int verificaCopia(Livro *l) {
    return l->copias;
}