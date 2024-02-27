package ATV_3.JAVA;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        KidsPlay kp = new KidsPlay();

        System.out.print("Digite a quantidade de jogos vendidos: ");
        int games = scan.nextInt();

        double profit = kp.totalProfit(games);
        double partSalary = kp.partSalary(profit, games);
        double totalSalary = kp.totalSalary(partSalary, games);

        System.out.printf("O valor total arrecadado foi: %d\nSalário sem bonus: %.2f\nCom bonus: %.2f", profit, partSalary, totalSalary);
        scan.close();
    }
}