package ATIVIDADE_2.JAVA;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Digite um numero: ");
        double n1 = scan.nextDouble();

        if (n1 % 2 == 0) {
            System.out.println("É par!");
        } 
        else {
            System.out.println("É impar!");
        }

        scan.close();
    }
}
