class Livro:
    def __init__(self, titulo, autor, numero_paginas, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.disponivel = disponivel
    
    def disponibilidade(self):
        if self.disponivel == True:
            print("Esse livro esta disponivel!!")
        else:
            print("Esse livro não está disponivel")

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            print("Livro empresado")
        else:
            print("Esse livro não está disponivel")

    def devolver(self):
        if self.disponivel == False:
            self.disponivel = True
            print("Livro devolvido com sucesso")
        else:
            print("Esse livro não está disponivel")

livro1 = Livro("Crepusculo", "Stephenie Meyer", 72, True)
livro1.disponibilidade()
livro1.emprestar()
livro1.devolver()