package ATV8_TIPOS_ABSTRATOS.java;

public class Empregado {
    private String nome;
    private long id;
    private String cargo;
    private double salario;
    private Departamento departamento;

    public Empregado(String nome, long id, String cargo, double salario, Departamento departamento) {
        this.nome = nome;
        this.id = id;
        this.cargo = cargo;
        this.salario = salario;
        this.departamento = departamento;
    }

    public void transferir(Departamento dep) {
        this.departamento = dep;
    }

    public String getDepInfo() {
        return this.departamento.depToString();
    }

    public void setNome(String name) {
        this.nome = name;
    }

    public void setCargo(String cg) {
        this.cargo = cg;
    }

    public void setSalario(double salary) {
        this.salario = salary;
    }

    public void changePersonalInfo(String name, String cg, double salary) {
        setNome(name);
        setCargo(cg);
        setSalario(salary);
    }

    public String empToString() {
        return "Nome: " + this.nome + "\nID: " + this.id + "\nCargo: " + this.cargo + "\nSalario: " + this.salario;
    }
}