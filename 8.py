class Carro:
    def __init__(self, marca, modelo, velocidade_atual):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_atual = velocidade_atual
    
    def acelerar(self):
        acelerar = float(input("Quanto quer acelerar:"))
        self.velocidade_atual += acelerar
        print(f"Voce esta á {self.velocidade_atual}km/h")
    
    def freiar(self):
        desacelerar = float(input("Quanto quer acelerar:"))
        self.velocidade_atual -= desacelerar
        print(f"Voce esta á {self.velocidade_atual}km/h")
    
    def carro_movimento(self):
        opcao = int(input("Carro ligado! para aperta o acelerador digite 1, para apertar o freio digite 2, para parar digite 3:"))
        while True:
            if opcao == 1:
                self.acelerar()
                opcao = int(input("Para mais acelerador digite 1, para apertar o freio digite 2, para parar digite 3:"))
            elif opcao == 2:
                self.freiar()
                opcao = int(input("Para acelerador digite 1, para apertar o freio digite 2, para parar digite 3:"))
            else:
                print("Carro parou!!!")
                break
                
corsa = Carro("fiat", 2010, 0)
corsa.carro_movimento()