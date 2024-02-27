package ATV_2.JAVA;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Pi pi = new Pi();

        System.out.print("Digite a quantidade de termos: ");
        int terms = scan.nextInt();

        double finalPi = pi.serieCalc(terms);

        System.out.printf("O valor de PI é %.5f", finalPi);

        scan.close();
    }
}