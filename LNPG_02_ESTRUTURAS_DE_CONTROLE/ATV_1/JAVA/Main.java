package ATV_1.JAVA;

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Airport air = new Airport();

        System.out.print("Quantidade de passageiros: ");
        int passengers = Integer.parseInt(scan.nextLine());

        for (int i = 1; i <= passengers; i++) {
            System.out.println("Passageiro " + i);

            System.out.print("RG? (Se sim, RG; Se não, Nao possui): ");
            String rg = scan.nextLine();

            System.out.print("Data de nascimento no RG (DD/MM/AAAA): ");
            String rgDate = scan.nextLine();

            System.out.print("Passagem? (Se sim, Passagem; Se não, Nao possui): ");
            String ticket = scan.nextLine();

            System.out.print("Data de nascimento na passagem (DD/MM/AAAA): ");
            String ticketDate = scan.nextLine();

            System.out.print("Assento (A12): ");
            String seat = scan.nextLine();

            if (air.checkRG(rg) == false) {
                System.out.println("A saída é nessa direção!");
            } else if (air.checkTicket(ticket) == false) {
                System.out.println("A recepção é nessa direção!");
            } else if (air.checkBirthDate(ticketDate, rgDate) == false) {
                System.out.println("190!");
            } else {
                System.out.printf("O seu assento é %s!", seat);
            }
        }
        scan.close();
    }
}