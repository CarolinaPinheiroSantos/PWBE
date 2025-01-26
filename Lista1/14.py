class MaquinaDeVendas:
    def __init__(self):
        self.produtos = {}
        self.dinheiro_insertido = 0

    def cadastrar_produto(self, nome, preco, quantidade):
        self.produtos[nome] = {"preco": preco, "quantidade": quantidade}

    def selecionar_produto(self, nome):
        if nome in self.produtos:
            preco = self.produtos[nome]["preco"]
            print(f"O preço do produto {nome} é {preco}")
            dinheiro = float(input("Digite o valor que você deseja inserir: "))
            self.dinheiro_insertido = dinheiro
            if dinheiro < preco:
                print("Dinheiro insuficiente.")
            else:
                troco = dinheiro - preco
                print(f"Troco: {troco}")
                self.produtos[nome]["quantidade"] -= 1
        else:
            print("Produto não encontrado.")

    def exibir_estoque(self):
        for nome, dados in self.produtos.items():
            print(f"{nome}: {dados['quantidade']} em estoque")
    
maquina = MaquinaDeVendas()
maquina.cadastrar_produto("Bolo", 5, 10)
maquina.cadastrar_produto("Dolritos", 4, 8)
maquina.selecionar_produto("Bolo")
maquina.exibir_estoque()
