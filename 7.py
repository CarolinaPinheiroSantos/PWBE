import math
class Tringulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calculo_area(self):
        semi = (self.lado1 + self.lado2 + self.lado3) // 2
        formula = semi * (semi - self.lado1) * (semi - self.lado2) * (semi - self.lado3)
        print(f"A area do triangulo é {math.sqrt(formula)}")
        
    def validar(self):
        if (self.lado1 + self.lado2 > self.lado3 and 
            self.lado1 + self.lado3 > self.lado2 and 
            self.lado2 + self.lado3 > self.lado1):
            self.calculo_area()
        else:
            print("Não é um triangulo")

triangulo1 = Tringulo(0, 10, 10)
triangulo1.validar()