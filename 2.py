class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo

    def deposito(self):
        print(f"Seu saldo atual da conta é {self.saldo}")
        escolha = int(input("Para fazer deposito digite 1 e para sair digite 2:"))
        while True:
            if escolha == 1:
                deposito = float(input("Qual valor: "))
                self.saldo += deposito
                print(f"Saldo: {self.saldo}")
                escolha = int(input("Para fazer novo deposito digite 1 e para sair digite 2:"))
            else:
                break
        print(self.saldo)

    def saque(self):
        print(f"Seu saldo atual da conta é {self.saldo}")
        escolha = int(input("Para fazer saque digite 1 e para sair digite 2:"))
        while True:
            if escolha == 1:
                deposito = float(input("Qual valor: "))
                self.saldo -= deposito
                print(f"Saldo: {self.saldo}")
                escolha = int(input("Para fazer novo saque digite 1 e para sair digite 2:"))
            else:
                break
        print(self.saldo)
    
cliente1 = ContaBancaria(256, "Carolina", 100)
cliente1.deposito()
cliente1.saque()