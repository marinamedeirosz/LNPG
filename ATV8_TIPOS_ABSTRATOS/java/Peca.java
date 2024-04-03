package ATV8_TIPOS_ABSTRATOS.java;

public class Peca {
    private String tipo;
    private String cor;
    private int[] posicao;

    public Peca(String tipo, String cor, int[] posicao) {
        this.tipo = tipo;
        this.cor = cor;
        this.posicao = posicao;
    }

    public void moverPeca(int[] pos) {
        this.posicao = pos;
    }

    public void capturaPeca() {
        this.posicao = null;
    }

    public boolean vericaMovimento(String type, int[] pos) {
        int linha = this.posicao[0];
        int coluna = this.posicao[1];
        int linhaNova = pos[0];
        int colunaNova = pos[1];
        int difLinha = linha - linhaNova;
        int difColuna = coluna - colunaNova;

        switch (type) {
            case "rei":
                return (difLinha <= 1 && difColuna <= 1);
            case "rainha":
                return (linha == linhaNova || coluna == colunaNova || difLinha == difColuna);
            case "torre":
                return (linha == linhaNova || coluna == colunaNova);
            case "bispo":
                return (difLinha == difColuna);
            case "cavalo":
                return ((difLinha == 2 && difColuna == 1) || (difLinha == 1 && difColuna == 2));
            case "peao":
                return (coluna == colunaNova && difLinha == 1);
            default:
                return false;
        }
    }

    @Override
    public String toString() {
        return "Tipo: " + this.tipo + "\nCor: " + this.cor + "\nPosicao: " + this.posicao[0] + "x" + this.posicao[1];
    }
}
