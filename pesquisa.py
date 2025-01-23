#Herança
#Herança em orientação ao objeto é uma Sub classe herdar, adicionar atributos e métodos novos ou modificar os existentes de uma Super classe.

class Aprendiz:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def trabalhar(self):
        print(f"{self.nome} esta estudando")

    def salario(self):
        print(f"O aprendiz recebe {self.salario}")


class Instrutor(Aprendiz):
    def __init__(self, nome, idade, salario, materia):
        super().__init__(nome, idade, salario)
        self.materia = materia
    
    def trabalhar(self):
        print(f"{self.nome} esta dando aula")

    def salario(self):
        print(f"O intrutor recebe {self.salario}")

aprendiz1 = Aprendiz("Carol", 18, 1400)
instrutor1 = Instrutor("Luca", 25, 5000, "python")

aprendiz1.trabalhar()
instrutor1.trabalhar()
