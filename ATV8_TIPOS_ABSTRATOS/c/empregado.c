#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Departamento;

typedef struct
{
    char nome[50];
    int id;
    char cargo[20];
    double salario;
    struct Departamento *departamento;
} Empregado;

typedef struct
{
    Empregado *empregados;
    char nome[50];
    int id;
    char localizacao[30];
} Departamento;

void inicializarEmpregado(Empregado *e, char nome[50], int id, char cargo[20], double salario, Departamento *departamento)
{
    strncpy(e->nome, nome, sizeof(e->nome) - 1);
    e->nome[sizeof(e->nome) - 1] = '\0';
    e->id = id;
    strncpy(e->cargo, cargo, sizeof(e->cargo) - 1);
    e->cargo[sizeof(e->cargo) - 1] = '\0';
    e->salario = salario;
    e->departamento = departamento;
}
void inicializarDepartamento(Departamento *d, char nome[50], int id, char localizacao[30])
{
    strncpy(d->nome, nome, sizeof(d->nome) - 1);
    d->nome[sizeof(d->nome) - 1] = '\0';
    d->id = id;
    strncpy(d->localizacao, localizacao, sizeof(d->localizacao) - 1);
    d->localizacao[sizeof(d->localizacao) - 1] = '\0';
}
void setNome(Empregado *e, char nome[50])
{
    strncpy(e->nome, nome, sizeof(e->nome) - 1);
    e->nome[sizeof(e->nome) - 1] = '\0';
}
void setCargo(Empregado *e, char cargo[20])
{
    strncpy(e->cargo, cargo, sizeof(e->cargo) - 1);
    e->cargo[sizeof(e->cargo) - 1] = '\0';
}
void setId(Empregado *e, int id)
{
    e->id = id;
}
void changePersonalData(Empregado *e, char nome[50], char cargo[20], int id)
{
    setNome(e, nome);
    setCargo(e, cargo);
    setId(e, id);
}
void transferirEmpregado(Empregado *e, Departamento *dep)
{
    e->departamento = dep;
}
/* Departamento * */ void getDepartamento(Empregado *e)
{
    /* return e->departamento; */
    printf("%s", e->departamento->nome);
    printf("%d", e->departamento->id);
    printf("%s", e->departamento->localizacao);
}
void addEmpregado(Empregado *e, Departamento *depart)
{
    depart->empregados = realloc(depart->empregados, sizeof(Empregado));
    depart->empregados[0] = *e;
}
void removeEmpregado(Empregado *e, Departamento *depart)
{
    for (int i = 0; i < sizeof(depart->empregados); i++)
    {
        if (depart->empregados[i].id == e->id)
        {
            for (int j = i; j < sizeof(depart->empregados) - 1; j++)
            {
                depart->empregados[j] = depart->empregados[j + 1];
            }
            depart->empregados =
                realloc(depart->empregados, sizeof(Empregado) * (sizeof(depart->empregados) - 1));
        }
    }
}
void infoEmpregados(Departamento *d)
{
    for (int i = 0; i < sizeof(d->empregados); i++)
    {
        printf("Nome: %s\n", d->empregados[i].nome);
        printf("Id: %d\n", d->empregados[i].id);
        printf("Cargo: %s\n", d->empregados[i].cargo);
        printf("Salario: %f\n", d->empregados[i].salario);
    }
}