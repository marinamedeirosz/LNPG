#include <stdio.h>

int verificar_primo(int num) {
    if (num <= 1)
        return 0;
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0)
            return 0;
    }
    return 1;
}

int proximo_primo(int num) {
    num++;
    while (!verificar_primo(num))
        num++;
    return num;
}

void exibir_texto(const char *formato, ...) {
    va_list args;
    va_start(args, formato);
    vprintf(formato, args);
    va_end(args);
}

int main() {
    int n;
    exibir_texto("Digite um numero inteiro: ");
    scanf("%d", &n);
    int primo = n;
    if (verificar_primo(n) == 0) {
        primo = proximo_primo(n);
    }
    exibir_texto("O menor numero primo maior que %d eh: %d\n", n, primo);    
    return 0;
}