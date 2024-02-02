package ATIVIDADE_2.JAVA;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int count = 0;
        System.out.print("Digite um numero inteiro: ");
        int n1 = scan.nextInt();

        if (n1 == 2) {
            System.out.println("É primo!");
        } 
        else {
            for (int i = 2; i < n1; i++) {
                if (n1 % i == 0) {
                    count++;
                }            
            }
            if (count > 0) {
                System.out.println("Não é primo!");
            }
            else {
                System.out.println("É primo!");
            }
        }

        scan.close();
    }
}
