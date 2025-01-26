class LojaVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = {}
        self.carrinho = {}
        self.id = 1

    def cadastrar_produto(self):
        for i in range(0,2):
            id = self.id
            self.id += 1
            nome_produto = input("Qual nome do produto novo: ")
            valor_produto = int(input("Qual valor do produto: "))
            self.produtos[id] = {"nome": nome_produto, "valor": valor_produto}
        
        # for id, produto in self.produtos.items():
        #     nome = produto["nome"]
        #     valor = produto["valor"]
        #     print(f'ID: {id}, Nome: {nome}, Valor: {valor}')

    def gerar_carrinho(self):
        while True:
            opcao = int(input("Para adicionar no carrinho digite 1 e para sair digite 2: "))
            if opcao == 1 :
                for id, produto in self.produtos.items():
                    nome = produto["nome"]
                    valor = produto["valor"]
                    print(f'ID: {id}, Nome: {nome}, Valor: {valor}')
                escolha = int(input("Digite o id para adicionar no carrinho: "))
                qt = int(input("Digite a quantidade: "))
                if escolha in self.produtos:
                    if escolha in self.carrinho:
                            self.carrinho[escolha]["quantidade"] += qt
                    else:
                        self.carrinho[escolha] = {"nome": self.produtos[escolha]["nome"], 
                                                    "valor": self.produtos[escolha]["valor"], 
                                                    "quantidade": qt} 
                print("Resumo carrinho:\n")        
                for id, produto in self.carrinho.items():
                    nome = produto["nome"]
                    quantidade = produto["quantidade"]
                    total = valor * quantidade
                    print(f'Produto: {nome}, Quantidade: {quantidade}, Total: {total}')
            if opcao == 2:
                break

    def desconto(self, total_compra):
        while True:
            opcao = int(input("Tem cupom digite 1 se nao tiver digite 2:"))
            if opcao == 1:
                cupom = input("Qual o nome do cupom: ")
                if cupom == "desconto10":
                    total_compra -= total_compra * (10 / 100)
                if cupom == "desconto20":
                    total_compra -= total_compra * (20 / 100)
                opcao = int(input("Tem outro cupom digite 1 se nao tiver digite 2:"))
            if opcao == 2:
                print(f"Total da compra: {self.total_compra}")
                break

    def total_compra(self):
        total_compra = sum(produto["valor"] * produto["quantidade"] for produto in self.carrinho.values())
        print(f"Total da compra: {total_compra}")
        self.desconto()


cliente1 = LojaVirtual("Carol")
cliente1.cadastrar_produto()
cliente1.gerar_carrinho()
cliente1.total_compra()