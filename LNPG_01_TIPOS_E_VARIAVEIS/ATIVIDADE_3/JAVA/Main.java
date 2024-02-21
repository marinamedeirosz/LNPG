package ATIVIDADE_3.JAVA;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Thermometer term = new Thermometer();

        System.out.print("Digite a temperatura em °C: ");
        double c = scan.nextDouble();
        term.transform(c);

        scan.close();
    }
}