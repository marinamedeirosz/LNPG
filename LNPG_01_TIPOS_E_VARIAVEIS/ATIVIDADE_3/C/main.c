#include <stdio.h>

int main() {
    double c;

    printf("Digite a temperatura em °C: ");
    scanf("%lf", &c);
  
    double f = c * 1.8 + 32;
    printf("A temperatura em °F é: %.2lf\n", f);
  
    return 0;
}