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

    public String depToString() {
        return "Nome: " + this.nome + "\nID: " + this.id + "\nLocalizacao: " + this.localizacao;
    }

    public void getEmpInfo() {
        if (this.empregados.size() != 0) {
            for (int i = 0; i < this.empregados.size(); i++) {
                this.empregados.get(i).empToString();
                /*
                 * this.empregados.forEach((empregado) -> {
                 * System.out.println(empregado.empToString());
                 * });
                 */
            }
        } else {
            System.out.println("Nao ha empregados no departamento");
        }
    }
}