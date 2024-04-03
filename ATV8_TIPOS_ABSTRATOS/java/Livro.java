package ATV8_TIPOS_ABSTRATOS.java;

public class Livro {
    private String titulo;
    private String autor;
    private int ano;
    private int copias;

    public Livro(String titulo, String autor, int ano, int copias) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
        this.copias = copias;
    }

    public void emprestaCopia() {
        this.copias--;
    }

    public void devolveCopia() {
        this.copias++;
    }

    public int verificaCopia() {
        return this.copias;
    }

    @Override
    public String toString() {
        return "Título: " + this.titulo + "\nAutor: " + this.autor + "\nAno: " + this.ano;
    }
}