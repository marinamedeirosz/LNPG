package ATV_5.JAVA;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class IPCA {
    protected List<List<String>> getIpcaData(Scanner scan) {
        List<List<String>> ipcaStorage = new ArrayList<List<String>>();
        System.out.println("\nAno/mês e o índice do IPCA (separados por espaço ' ') e '*' para parar: ");

        while (true) {
            String input = scan.nextLine();
            if (input.equals("*")) {
                break;
            }
            String[] dataArray = input.split(" ");
            List<String> data = new ArrayList<>();
            data.add(dataArray[0]);
            data.add(dataArray[1].replace(",", "."));

            ipcaStorage.add(data);
        }
        return ipcaStorage;
    }

    protected List<List<String>> rankedIpca(List<List<String>> ipca) {
        ipca.sort((p1, p2) -> p1.get(1).compareTo(p2.get(1)));
        return ipca;
    }

    protected double ipcaAverage(List<List<String>> ipca) {
        double sum = 0;
        double average = sum / (ipca.size());
        for (List<String> item : ipca) {
            sum += Double.parseDouble(item.get(1));
        }
        return average;
    }
}