import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class ControleEstoque {
    private static Map<String, Integer> estoque = new HashMap<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        while (true) {
            exibirMenu();
            optionMenu();
        }
    }

    private static void adicionarProduto() {
        String nome = getString("Digite o nome do produto:");
        while (true) {
            int quantidade = getInt("Digite a quantidade do produto:");
            if (quantidade > 0) {
                if (estoque.containsKey(nome)) {
                    quantidade += estoque.get(nome);
                }
                estoque.put(nome, quantidade);
                exibirTexto("Produto adicionado com sucesso!");
                break;
            } else {
                exibirTexto("Valor negativo! Digite um valor válido!");
            }
        }
    }

    private static void venderProduto() {
        String nome = getString("Digite o nome do produto:");
        int quantidade = getInt("Digite a quantidade a ser vendida:");
        if (estoque.containsKey(nome)) {
            int estoqueAtual = estoque.get(nome);
            if (estoqueAtual >= quantidade) {
                estoque.put(nome, estoqueAtual - quantidade);
                exibirTexto("Venda realizada com sucesso!");
            } else {
                exibirTexto("Quantidade insuficiente em estoque!");
            }
        } else {
            exibirTexto("Produto não encontrado em estoque!");
        }
    }

    private static void exibirEstoque() {
        exibirTexto("Estoque atual:");
        for (String produto : estoque.keySet()) {
            int quantidade = estoque.get(produto);
            exibirTexto(produto + ": " + quantidade);
        }
    }

    private static void exibirTexto(String text) {
        System.out.println(text);
    }

    private static void exibirMenu() {
        exibirTexto("Escolha uma opção:");
        exibirTexto("1 - Adicionar Produto");
        exibirTexto("2 - Vender Produto");
        exibirTexto("3 - Exibir Estoque");
        exibirTexto("4 - Sair");
    }

    private static void optionMenu() {
        int opcao = getInt("Opcao desejada: ");
        switch (opcao) {
            case 1:
                adicionarProduto();
                break;
            case 2:
                venderProduto();
                break;
            case 3:
                exibirEstoque();
                break;
            case 4:
                exibirTexto("Saindo do programa...");
                return;
            default:
                exibirTexto("Opção inválida!");
        }
    }

    private static String getString(String text) {
        exibirTexto(text);
        String str = scanner.nextLine();
        return str;
    }

    private static int getInt(String text) {
        exibirTexto(text);
        int number = Integer.parseInt(scanner.nextLine());
        return number;
    }
}