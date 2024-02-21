package ATIVIDADE_1.JAVA;

public class Calculator {
    protected double sum(double n1, double n2) {
        double soma = n1 + n2;
        return soma;
    }

    protected double sub(double n1, double n2) {
        double subtracao = n1 - n2;
        return subtracao;
    }

    protected double mult(double n1, double n2) {
        double multiplicacao = n1 * n2;
        return multiplicacao;
    }

    protected double div(double n1, double n2) {
        double divisao = n1 / n2;
        return divisao;
    }

    protected void show(double n1, double n2) {
        String[] options = { "Soma: ", "Subtração: ", "Multiplição: ", "Divisão: " };
        Double[] results = { sum(n1, n2), sub(n1, n2), mult(n1, n2), div(n1, n2) };

        for (int i = 0; i < 4; i++) {
            System.out.println(options[i] + results[i]);
        }
    }
}