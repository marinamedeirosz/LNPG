package ATIVIDADE_4.JAVA;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Adulthood checker = new Adulthood();

        System.out.print("Digite sua idade: ");
        int age = scan.nextInt();
        checker.checkAge(age);

        scan.close();
    }
}