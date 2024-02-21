package ATIVIDADE_5.JAVA;

public class Average {
    double sum = 0;
    double weights = 0;

    protected double scoreWithWeight(double score, double weight) {
        double mult = score * weight;
        sumWithWeight(mult);
        sumWeights(weight);
        return mult;
    }

    protected void sumWithWeight(double n) {
        sum += n;
    }

    protected double getSumWithWeight() {
        return sum;
    }

    protected void sumWeights(double p) {
        weights += p;
    }

    protected double getSumWeights() {
        return weights;
    }

    protected double finalScore(double s, double w) {
        double result = s / w;
        return result;
    }
}