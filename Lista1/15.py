import random

class Carta:
    def __init__(self, cor, valor):
        self.cor = cor
        self.valor = valor
        
    def __repr__(self):
        return f"{self.valor} de {self.cor}"
    
class Baralho:
    def __init__(self):
        cores = ['Vermelho', 'Azul', 'Amarelo', 'Verde']
        valores = ['1','2', '3', '4', '5', '6', '7', '8', '9']
        self.cartas = [Carta(cor, valor) for cor in cores for valor in valores]
        random.shuffle(self.cartas)
        
    def distribuir(self, qtd):
        mao = self.cartas[:qtd]
        mao2 = self.cartas[qtd:qtd*2]
        return mao, mao2
    
    def jogar(self, mao, mao2):
        while len(mao) > 0 and len(mao2) > 0:
            if len(mao) > 0:
                print(f"Mão do Jogador 1: {mao}")
                escolha = int(input("Escolha uma carta pelo número (1 a {0}): ".format(len(mao)))) - 1
                if 0 <= escolha < len(mao):
                    print(f"Jogador 1 jogou a carta: {mao.pop(escolha)}")
                    mao.pop(escolha)
                    print(mao)
            else:
                print("ganhou")

baralho = Baralho()
mao, mao2 = baralho.distribuir(7)
baralho.jogar(mao, mao2)
