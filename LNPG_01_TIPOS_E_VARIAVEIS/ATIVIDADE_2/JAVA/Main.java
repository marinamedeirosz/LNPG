package ATIVIDADE_2.JAVA;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Even even = new Even();

        System.out.print("Digite um numero: ");
        double n1 = scan.nextDouble();
        even.isEven(n1);

        scan.close();
    }
}