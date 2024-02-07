#include <stdio.h>

void parOuImpar(n1) {
  if (n1 % 2 == 0){
    printf("É par!");
  } else {
    printf("É impar!");
  }
};


int main() {
  double n1;

  printf("Digite um número: ");
  scanf("%lf", &n1);
  parOuImpar(n1);

  return 0;
}