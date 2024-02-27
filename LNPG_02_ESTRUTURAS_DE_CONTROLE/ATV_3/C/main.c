#include <stdio.h>
#include <math.h>

int main()
{
    int games;

    printf("Digite a quantidade de jogos vendidos: ");
    scanf("%d", &games);

    double gameValue = 19.9;
    double totalProfit = gameValue * games;
    double partSalary = totalProfit / 2;
    double totalSalary = floor(games / 15) * (totalProfit * 0.08) + partSalary;

    printf("Total arrecadado: %.2f\nSalario sem bonus: %.2f\nCom bonus: %.2f\n", totalProfit, partSalary, totalSalary);

    return 0;
} 