package ATV_3.JAVA;

public class KidsPlay {
    protected double totalProfit(int games) {
        double gameValue = 19.9;
        double total = gameValue * games;
        return total;
    }

    protected double partSalary(double total, int games) {
        double totalGames = totalProfit(games);
        double pSalary = totalGames * 0.5;
        return pSalary;
    }

    protected double totalSalary(double partSalary, int games) {
        double bonus = Math.floor(games/15) * (partSalary * 2) * 0.08;
        double salary = partSalary + bonus;
        return salary;
    }
}