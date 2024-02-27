package ATV_2.JAVA;

public class Pi {
    protected double serieCalc(int terms) {
        double s = 0;
        boolean operator = true;
        int count = 1;
        for (int i = 0; i < terms; i++) {
            if (operator) {
                s += 1 / (Math.pow((count), 3));
            } else {
                s -= 1 / (Math.pow((count), 3));
            }
            count += 2;
            operator = !operator;
        }
        double pi = Math.cbrt(s * 32);
        return pi;
    }
}