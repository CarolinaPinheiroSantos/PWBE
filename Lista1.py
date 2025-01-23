#Lista de Exercicios PWBE - 23/01 e 24/01
#1
# class Circulo:
#     def __init__(self,  raio):
#         self.raio = raio

#     def calculo_area(self):
#         formula =  (self.raio ** 2) * 3.1415
#         print(f"A area do circulo é {formula}")

#     def calculo_perimetro(self):
#         formula = (2 * 3.1415) * self.raio
#         print(f"O perimetro do circulo é {formula}")
    
# circulo1 = Circulo(5)
# circulo1.calculo_area()
# circulo1.calculo_perimetro()


#2
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