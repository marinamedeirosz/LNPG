import java.util.ArrayList;

public class ListaDeCompras {
    public static void main(String[] args) {
        ListaDeCompras lista = new ListaDeCompras();
        lista.adicionarItem("Maçã");
        lista.adicionarItem("Banana");
        lista.adicionarItem("Pêra");
        lista.adicionarItem("Banana");
        lista.removerItem("Banana");
        lista.removerItem("Laranja");
        lista.exibirLista();
    }

    private ArrayList<String> itens;

    public ListaDeCompras() {
        this.itens = new ArrayList<>();
    }

    public ArrayList<String> getItens() {
        return this.itens;
    }

    public void adicionarItem(String item) {
        if (item == null) {
            exibirTexto("O item não pode ser nulo.");
            return;
        }
        if (!itens.contains(item)) {
            itens.add(item);
        } else {
            exibirTexto(item + " já está na lista");
        }
    }

    public void removerItem(String item) {
        if (item == null) {
            exibirTexto("O item não pode ser nulo.");
            return;
        }
        if (itens.contains(item)) {
            itens.remove(item);
        } else {
            exibirTexto(item + " não está na lista");
        }
    }

    public void exibirLista() {
        ArrayList<String> items = getItens();
        if (items.isEmpty()) {
            exibirTexto("A lista está vazia");
        } else {
            exibirTexto("Lista de Compras:");
            for (String item : itens) {
                System.out.println("- " + item);
            }
        }
    }

    private static void exibirTexto(String text) {
        System.out.println(text);
    }
}