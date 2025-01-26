class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []
        
    def situacao_aluno(self):
        media = 0
        for i in range(0,5):
            nota = float(input("Digite sua nota: "))
            self.notas.append(nota)

        media = sum(self.notas) / 5
        if media >= 5:
            print("Aprovado")
        elif media < 5 and media > 2.5:
            print("Recuperação")
        else:
            print("Reprovado")
            
aluno1 = Aluno("Laura", 1023)
aluno1.situacao_aluno()