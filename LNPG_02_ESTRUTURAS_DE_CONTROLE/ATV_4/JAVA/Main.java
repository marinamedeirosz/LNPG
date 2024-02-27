package ATV_4.JAVA;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Vestibular vb = new Vestibular();
        List<List<String>> participants = new ArrayList<>();

        System.out.println("Gabarito (10 numeros separados por espaço ' '): ");
        String input = scan.nextLine();
        String[] answers = vb.getAnswers(input);
        List<List<String>> updatedParticipants = vb.getParticipantsData(participants, scan);
        List<List<String>> answersList = vb.getGrades(answers, updatedParticipants);
        List<List<String>> alphabeticGrades = vb.alphabeticOrder(answersList);
        List<List<String>> orderedGrades = vb.rankedGrades(answersList);
        double approvedPercentage = vb.approvedPercentage(alphabeticGrades);

        System.out.println("Relação dos participantes em ordem alfabética com suas respectivas notas: ");
        vb.printList(alphabeticGrades);

        System.out.println("\nParticipante com a melhor pontuação: ");
        System.out.printf("Nome: %s Nota: %s\n", (orderedGrades.get(0)).get(0), (orderedGrades.get(0)).get(1));

        System.out.println("\nParticipante com a pior pontuação: ");
        System.out.printf("Nome: %s Nota: %s\n", (orderedGrades.get(orderedGrades.size() - 1)).get(0), (orderedGrades.get(orderedGrades.size() - 1)).get(1));

        System.err.printf("\nPercentual de participantes com mais da metade de questões certas: %.1f", approvedPercentage);

        scan.close();
    }
}