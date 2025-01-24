class LojaVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = {}
        self.carinho = {}
        self.id = 1

    def cadastrar_produto(self):
        for i in range(0,2):
            id = self.id
            self.id += 1
            nome_produto = input("Qual nome do produto novo: ")
            valor_produto = int(input("Qual valor do produto: "))
            self.produtos[id] = {"nome": nome_produto, "valor": valor_produto}
        
        for id, produto in self.produtos.items():
            nome = produto["nome"]
            valor = produto["valor"]
            print(f'Chave: {id}, Nome: {nome}, Valor: {valor}')

cliente1 = LojaVirtual("Carol")
cliente1.cadastrar_produto()