package ATIVIDADE_5.JAVA;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Average av = new Average();
        double value;
        double weight;

        for (int i = 1; i < 4; i++) {
            System.out.printf("Digite a %d° nota: ", i);
            value = scan.nextDouble();
            System.out.printf("Digite o peso da %d° nota: ", i);
            weight = scan.nextDouble();
            av.scoreWithWeight(value, weight);
        }
        double sum = av.getSumWithWeight();
        double weights = av.getSumWeights();
        System.out.printf("A média ponderada das notas é: %.2f", av.finalScore(sum, weights));

        scan.close();
    }
}