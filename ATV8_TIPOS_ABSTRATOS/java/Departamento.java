package ATV8_TIPOS_ABSTRATOS.java;


import java.util.ArrayList;

public class Departamento {
    private ArrayList<Empregado> empregados;
    private String nome;
    private long id;
    private String localizacao;

    public Departamento(ArrayList<Empregado> empregados, String nome, long id, String localizacao) {
        this.empregados = empregados;
        this.nome = nome;
        this.id = id;
        this.localizacao = localizacao;
    }
    public void addEmpregado(Empregado empregado) {
        this.empregados.add(empregado);
    }
    public void removeEmpregado(Empregado empregado) {
        this.empregados.remove(empregado);
    }
    public ArrayList<Empregado> getEmpregados() {
        return this.empregados;
    }
}