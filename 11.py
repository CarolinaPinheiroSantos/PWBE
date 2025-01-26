class Banco:
    def __init__(self):
        self.cliente = []
        self.conta = {}

    def cadastrar_cliente(self):
        nome = input("Digite seu nome: ")
        cpf = int(input("Digite seu CPF: "))
        cliente = {"nome": nome, "cpf": cpf} 
        self.cliente.append(cliente)
        print("Cadastro sucesso")
        return cliente

    def cadastrar_conta(self, cliente):
        numero_conta = int(input("Digite numero da conta(de 0 ate 20): "))
        conta = {"cliente": cliente, "numero_conta": numero_conta, "saldo": 0}
        self.conta[numero_conta] = conta
        print("Cadastro sucesso")
        return numero_conta
    
    def depositar(self, numero_conta):
        valor = int(input("Qual valor quer depositar: "))
        if valor > 0:
            self.conta[numero_conta]["saldo"] += valor
            print(f"Depósito de R${valor} realizado com sucesso. Saldo atual: {self.conta[numero_conta]["saldo"]} reais")
        else:
            print("Valor de depósito deve ser positivo.")
    
    def sacar(self, numero_conta):
        valor = int(input("Qual valor quer sacar:"))
        if numero_conta in self.conta:
            if valor > 0:
                if self.conta[numero_conta]["saldo"] >= valor:
                    self.conta[numero_conta]["saldo"] -= valor
                    print(f"Saque de R${valor} realizado com sucesso. Saldo atual: {self.conta[numero_conta]["saldo"]} reais")
                else:
                    print("Saldo insuficiente.")
            else:
                print("Valor de saque deve ser positivo.")

    def tranferir(self):
        conta_descontada = int(input("Qual numero da conta que ira tranferir: "))
        valor = int(input("Qual valor quer tranferir:"))
        conta_recebe = int(input("Qual numero da conta que ira receber: "))
        if conta_descontada in self.conta and conta_recebe in self.conta:
            if valor > 0:
                self.conta[conta_descontada]["saldo"] -= valor
                self.conta[conta_recebe]["saldo"] += valor
                print(f"Transferencia de R${valor} realizado com sucesso. Saldo atual {self.conta[conta_descontada]["cliente"]}: {self.conta[conta_descontada]["saldo"]} reais e Saldo atual {self.conta[conta_descontada]["cliente"]}: {self.conta[conta_recebe]["saldo"]} reais")
            else:
                    print("Saldo insuficiente.")
        else:
            print("Valor de saque deve ser positivo.")

    def saldo(self):
        for i in self.conta:
            print(i)
    
banco = Banco()
cliente1 = banco.cadastrar_cliente() 
numero_conta1 = banco.cadastrar_conta(cliente1)  
banco.depositar(numero_conta1)  
banco.sacar(numero_conta1)

cliente2 = banco.cadastrar_cliente()  
numero_conta2 = banco.cadastrar_conta(cliente2)  
banco.depositar(numero_conta2) 
banco.sacar(numero_conta2) 
 
banco.tranferir()
banco.saldo()
