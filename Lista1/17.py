class Biblioteca:
    def __init__(self):
        self.livros = {}

    def cadastrar_livro(self, titulo, autor, quantidade):
        self.livros[titulo] = {"autor": autor, "quantidade": quantidade, "disponivel": quantidade}

    def emprestar_livro(self, titulo):
        if titulo in self.livros:
            if self.livros[titulo]["disponivel"] > 0:
                self.livros[titulo]["disponivel"] -= 1
                print(f"Você pegou o livro {titulo}.")
            else:
                print(f"O livro {titulo} não está disponível no momento.")
        else:
            print(f"O livro {titulo} não existe na biblioteca.")

    def devolver_livro(self, titulo):
        if titulo in self.livros:
            self.livros[titulo]["disponivel"] += 1
            print(f"Você devolveu o livro {titulo}.")
        else:
            print(f"O livro {titulo} não foi registrado na biblioteca.")

    def verificar_disponibilidade(self, titulo):
        if titulo in self.livros:
            if self.livros[titulo]["disponivel"] > 0:
                print(f"O livro {titulo} está disponível.")
            else:
                print(f"O livro {titulo} está indisponível.")
            
biblioteca = Biblioteca()
biblioteca.cadastrar_livro("Crepusculo", "sla", 100)
biblioteca.emprestar_livro("Crepusculo")
biblioteca.devolver_livro("Crepusculo")
biblioteca.verificar_disponibilidade("Blabla")