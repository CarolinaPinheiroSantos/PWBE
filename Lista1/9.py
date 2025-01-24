class Paciente:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico = []
        
    def adicionar_consulta(self):
        opcao = input("Quer fazer uma consulta(s/n):")
        while True:
            if opcao == "s":
                nova_consulta = input("Qual consulta deseja fazer:")
                self.historico.append(nova_consulta)
                opcao = input("Quer fazer uma consulta(s/n):")
            else:
                break
        
    def consultas_realizadas(self):
        print(f"Seu historico de exames feitos:\n {self.historico}")
        
paciente1 = Paciente("Luciana", 50)
paciente1.adicionar_consulta()
paciente1.consultas_realizadas()