package ATIVIDADE_1.JAVA;
import java.util.Scanner;


class Main{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Digite o primeiro numero: ");
        double n1 = scan.nextDouble();

        System.out.print("Digite o segundo numero: ");
        double n2 = scan.nextDouble();

        Calculadora calc = new Calculadora();

        System.out.print("Soma: ");
        System.out.println(calc.sum(n1, n2));
        System.out.print("Subtração: ");
        System.out.println(calc.sub(n1, n2));
        System.out.print("Multiplicação: ");
        System.out.println(calc.mult(n1, n2));
        System.out.print("Divisão: ");
        System.out.println(calc.div(n1, n2));

        scan.close();
    }
}