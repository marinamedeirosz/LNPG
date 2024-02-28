package ATV_5.JAVA;

import java.util.Scanner;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        IPCA ipca = new IPCA();

        List<List<String>> ipcaData = ipca.getIpcaData(scan);
        List<List<String>> orderedIpca = ipca.rankedIpca(ipcaData);
        double ipcaAvg = ipca.ipcaAverage(orderedIpca);
        List<String> lowestIpca = orderedIpca.get(orderedIpca.size() - 1);
        List<String> highestIpca = orderedIpca.get(0);

        System.out.printf("Menor valor do IPCA: %s  Mês/ano: (%s)\n", lowestIpca.get(1), lowestIpca.get(0));
        System.out.printf("Maior valor do IPCA: %s  Mês/ano: (%s)\n", highestIpca.get(1), highestIpca.get(0));
        System.out.printf("Média de todos os valores do IPCA: %.2f\n", ipcaAvg);

        scan.close();
    }
}