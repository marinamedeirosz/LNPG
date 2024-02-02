package ATIVIDADE_4.JAVA;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        System.out.print("Digite sua idade: ");
        int idade = scan.nextInt();
        
        if (idade >= 18) {
            System.out.println("Você é maior de idade!");
        }
        else {
            System.out.println("Você é menor de idade!");
        }

        scan.close();
    }
}
