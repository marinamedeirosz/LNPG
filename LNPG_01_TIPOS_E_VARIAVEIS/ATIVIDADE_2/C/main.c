#include <stdio.h>

double primo(n1) {
  int count = 0;
  
  if (n1 == 2){
    printf("É primo!");
  } else {
    for (int i = 2; i < n1; i++) {
      if (n1 % i == 0) {
        count++;
      }
    }
    if (count > 0){
      printf("Não é primo!");
    } else{
      printf("É primo!");
    }
    }
};


int main() {
    double n1;

    printf("Digite o primeiro número: ");
    scanf("%lf", &n1);
    primo(n1);
  
    return 0;
}