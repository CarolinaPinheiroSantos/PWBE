class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calculo_area(self):
        formula =  self.largura * self.altura
        print(f"A area do retangulo é {formula}m²")

    def calculo_perimetro(self):
        formula = 2 * (self.largura + self.altura)
        print(f"O perimetro do retangulo é {formula}m")
    
retangulo1 = Retangulo(5, 3)
retangulo1.calculo_area()
retangulo1.calculo_perimetro()