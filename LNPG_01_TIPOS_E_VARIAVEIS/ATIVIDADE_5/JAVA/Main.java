package ATIVIDADE_5.JAVA;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        System.out.print("Digite a 1° nota: ");
        double n1 = scan.nextDouble();
        System.out.print("Digite o peso da 1° nota: ");
        double p1 = scan.nextDouble();

        System.out.print("Digite a 2° nota: ");
        double n2 = scan.nextDouble();
        System.out.print("Digite o peso da 2° nota: ");
        double p2 = scan.nextDouble();

        System.out.print("Digite a 3° nota: ");
        double n3 = scan.nextDouble();
        System.out.print("Digite o peso da 3° nota: ");
        double p3 = scan.nextDouble();

        double media = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3);

        System.out.print("A média ponderada das notas é: ");
        System.out.println(media);

        scan.close();
    }
}
