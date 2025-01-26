class Agenda:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, numero):
        self.contatos[nome] = numero

    def editar_contato(self, nome, novo_nome, novo_numero):
        if nome in self.contatos:
            self.contatos[novo_nome] = novo_numero
            del self.contatos[nome]
        else:
            print("Contato não encontrado.")

    def remover_contato(self, nome):
        del self.contatos[nome]

    def buscar_por_nome(self, nome):
        if nome in self.contatos:
            return self.contatos[nome]
        else:
            print("Contato não encontrado.")
            return None

    def buscar_por_numero(self, numero):
        for nome, num in self.contatos.items():
            if num == numero:
                return nome
        return "Contato não encontrado."

agenda = Agenda()
agenda.adicionar_contato("Carol", "123456789")
agenda.adicionar_contato("thata", "987654321")
print(agenda.buscar_por_nome("Carol"))
agenda.editar_contato("Carol", "Carol Pinheiro", "1111111")
agenda.remover_contato("thata")
print(agenda.buscar_por_numero("1111111"))
