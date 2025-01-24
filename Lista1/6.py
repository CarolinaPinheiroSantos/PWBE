class Produto:
    def __init__(self, nome, preço, quantidade_estoque):
        self.nome = nome
        self.preço = preço
        self.quantidade_estoque = quantidade_estoque
        
    def estoque(self):
        if self.quantidade_estoque > 0:
            print(f"Quantidade em estoque {self.quantidade_estoque}")
        else:
            print("Estoque indisponivel")
            
produto1 = Produto("Leite", 5.70, 0)
produto1.estoque()
            