#include <stdio.h>
#include <math.h>

double serieCalc(int terms)
{
	double pi, s = 0;
	int operator= 1;
	int count = 1;
	for (int i = 0; i < terms; i++)
	{
		if (operator== 1)
		{
			s += 1 / (pow((count), 3));
			operator= 0;
		}
		else
		{
			s -= 1 / (pow((count), 3));
			operator= 1;
		}
		count += 2;
	}
	pi = cbrt(s * 32);
	return pi;
};

int main()
{
	int terms;

	printf("Digite a quantidade de termos: ");
	scanf("%d", &terms);
	printf("Valor de pi: %.5f", serieCalc(terms));

	return 0;
}