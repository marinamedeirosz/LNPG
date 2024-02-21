package ATIVIDADE_3.JAVA;

public class Thermometer {
    protected void transform(double c) {
        double f = c * 1.8 + 32;
        System.out.println("A temperatura em farenheit é: " + f);
    }
}