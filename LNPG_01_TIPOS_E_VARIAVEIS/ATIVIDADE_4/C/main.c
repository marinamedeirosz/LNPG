#include <stdio.h>

int main() {
    double idade;

    printf("Digite sua idade: ");
    scanf("%lf", &idade);
  
    if (idade >= 18) {
        printf("Você é maior de idade!");
    } else {
      printf("Você é menor de idade!");
    }
  
    return 0;
}