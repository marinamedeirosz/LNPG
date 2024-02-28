#include <stdio.h>

int main()
{
  double n1;
  double p1;
  double n2;
  double p2;
  double n3;
  double p3;

  printf("Digite a primeira nota e seu peso, separando-as por um espaço: ");
  scanf("%lf"
        "%lf",
        &n1, &p1);
  printf("Digite a segunda nota e seu peso, separando-as por um espaço: ");
  scanf("%lf"
        "%lf",
        &n2, &p2);
  printf("Digite a terceira nota e seu peso, separando-as por um espaço: ");
  scanf("%lf"
        "%lf",
        &n3, &p3);

  double media = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3);
  printf("Sua média é: %.2lf", media);

  return 0;
}