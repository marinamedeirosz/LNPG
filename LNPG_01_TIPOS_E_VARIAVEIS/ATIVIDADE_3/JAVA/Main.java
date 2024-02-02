package ATIVIDADE_3.JAVA;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        System.out.print("Digite a temperatura em °C: ");
        double c = scan.nextDouble();

        double f = c * 1.8 + 32;
        System.out.print("A temperatura em farenheit é: ");
        System.out.println(f);

        scan.close();    
    }
}
