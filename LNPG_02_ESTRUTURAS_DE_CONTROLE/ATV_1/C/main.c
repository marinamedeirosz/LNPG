#include <stdio.h>
#include <string.h>

int checkRG(const char *rg)
{
	if (strcmp(rg, "RG") == 0)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

int checkTicket(const char *ticket)
{
	if (strcmp(ticket, "Passagem") == 0)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

int checkBirthDate(const char *ticketDate, const char *rgDate)
{
	if (strcmp(ticketDate, rgDate) == 0)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

int main()
{
	int passengers;
	char rg[11], rgDate[11], ticket[11], ticketDate[11], seat[4];

	printf("Quantidade de passageiros: ");
	scanf("%d", &passengers);

	for (int i = 1; i <= passengers; i++)
	{
		printf("\nPassageiro %d", i);

		printf("\nRG? (Se sim, RG; Se não, Nao possui): ");
		scanf(" %[^\n]", rg);

		printf("Data de nascimento no RG (DD/MM/AAAA): ");
		scanf(" %[^\n]", rgDate);

		printf("Passagem? (Se sim, Passagem; Se não, Nao possui): ");
		scanf(" %[^\n]", ticket);

		printf("Data de nascimento na passagem (DD/MM/AAAA): ");
		scanf(" %[^\n]", ticketDate);

		printf("Assento (A12): ");
		scanf(" %[^\n]", seat);

		if (checkRG(rg) == 0)
		{
			printf("A saida e nessa direcao");
		}
		else if (checkTicket(ticket) == 0)
		{
			printf("A recepção é nessa direção!");
		}
		else if (checkBirthDate(ticketDate, rgDate) == 0)
		{
			printf("190!");
		}
		else
		{
			printf("O seu assento é %s!", seat);
		}
	}

	return 0;
}