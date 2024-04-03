#include <stdio.h>

typedef struct Empregado{
    char[] nome;
    int id;
    char[] cargo;
    double salario;
    char[] departamento; 
};

typedef struct Departamento{
    struct Empregado[] empregados;
    char[] nome;
    int id;
    char[] localizacao;
};

void inicializar(Empregado *e, char[] nome, int id, char[] cargo, double salario, Departamento *departamento;) {
    e->nome = nome;
    e->id = id;
    e->cargo = cargo;
    e->salario = salario;
    e->departamento = *departamento;
}
void setNome(Empregado *e, char[] nome) {
    e->nome = nome;
}

void setCargo(Empregado *e, char[] cargo) {
    e->cargo = cargo;
}

void setId(Empregado *e, int id) {
    e->id = id;
}

void transferirEmpregado(Empregado *e, char[] dep) {
    e->departamento = dep;
}
char[] getDepartamento(Empregado *e) {
    return e->departamento;
}

void addEmpregado(Empregado *e, Departamento *depart) {
    d->empregados
}
void removeEmpregado(Empregado *e) {}
struct Empregado[] infoEmpregados(Departamento *d) {
    return d->empregados;
}
