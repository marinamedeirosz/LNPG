#include <stdio.h>

double soma(n1, n2)
{
  return n1 + n2;
};
double sub(n1, n2)
{
  return n1 - n2;
};
double mult(n1, n2)
{
  return n1 * n2;
};
double div(n1, n2)
{
  return n1 / n2;
};

int main()
{
  double n1;
  double n2;

  printf("Digite o primeiro número: ");
  scanf("%lf", &n1);
  printf("Digite o segundo número: ");
  scanf("%lf", &n2);

  printf("A soma dos números é: %.2f\n", soma(n1, n2));
  printf("A subtração dos números é: %.2f\n", sub(n1, n2));
  printf("A multiplicação dos números é: %.2f\n", mult(n1, n2));
  printf("A divisão dos números é: %.2f\n", div(n1, n2));

  return 0;
}