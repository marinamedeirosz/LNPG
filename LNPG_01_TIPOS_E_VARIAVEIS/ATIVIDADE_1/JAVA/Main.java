package ATIVIDADE_1.JAVA;

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Calculator calc = new Calculator();

        System.out.print("Digite o primeiro numero: ");
        double n1 = scan.nextDouble();

        System.out.print("Digite o segundo numero: ");
        double n2 = scan.nextDouble();

        calc.show(n1, n2);

        scan.close();
    }
}