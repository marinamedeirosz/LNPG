package ATV_4.JAVA;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Vestibular {
    protected String[] getAnswers(String input) {
        String[] answerList = input.split(" ");
        return answerList;
    }

    protected List<List<String>> getParticipantsData(List<List<String>> participants, Scanner scan) {
        System.out.println("\nNome e respostas (separados por espaço ' '): ");

        while (true) {
            String input = scan.nextLine();
            if (input.equals("*")) {
                break;
            }
            String[] dataArray = input.split(" ");
            List<String> data = new ArrayList<>();
            for (String item : dataArray) {
                data.add(item);
            }
            participants.add(data);
        }
        return participants;
    }

    protected List<List<String>> alphabeticOrder(List<List<String>> participants) {
        participants.sort((p1, p2) -> p1.get(0).compareTo(p2.get(0)));
        return participants;
    }

    protected List<List<String>> getGrades(String[] answers, List<List<String>> participants) {
        List<List<String>> answersList = new ArrayList<>();

        for (List<String> data : participants) {
            List<String> answer = new ArrayList<>();
            int score = 0;
            for (int i = 0; i < answers.length; i++) {
                if (answers[i].equals(data.get(i + 1))) {
                    score += 1;
                }
            }
            answer.add(data.get(0));
            answer.add(Integer.toString(score));
            answersList.add(answer);
        }
        return answersList;
    }

    protected List<List<String>> rankedGrades(List<List<String>> grades) {
        grades.sort((p1, p2) -> p1.get(1).compareTo(p2.get(1)));
        return grades;
    }

    protected double approvedPercentage(List<List<String>> grades) {
        int approvedStudents = 0;
        for (List<String> participant : grades) {
            if (Integer.parseInt(participant.get(1)) > 5) {
                approvedStudents += 1;
            }
        }
        double percentage = ((double) approvedStudents / grades.size()) * 100;
        return percentage;
    }

    protected void printList(List<List<String>> list) {
        for (List<String> participant : list) {
            System.out.printf("Nome: %s Nota: %s\n", participant.get(0), participant.get(1));
        }
    }
}