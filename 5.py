class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        
    def salario_liquido(self):
        imposto_FGTS = 100
        benefecio_refeicao = 200
        beneficio_clube = 50
        print(f"Seu salario liquido será de {self.salario - imposto_FGTS - benefecio_refeicao - beneficio_clube}")

funcionario1 = Funcionario("Thalita", 1500, "Aprendiz de desing")
print(f"A funcionaria/o {funcionario1.nome} tem salario bruto de {funcionario1.salario}")        
funcionario1.salario_liquido()
