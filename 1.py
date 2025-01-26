# Lista de Exercicios PWBE - 23/01 e 24/01

class Circulo:
    def __init__(self,  raio):
        self.raio = raio

    def calculo_area(self):
        formula =  (self.raio ** 2) * 3.1415
        print(f"A area do circulo é {formula}")

    def calculo_perimetro(self):
        formula = (2 * 3.1415) * self.raio
        print(f"O perimetro do circulo é {formula}")
    
circulo1 = Circulo(5)
circulo1.calculo_area()
circulo1.calculo_perimetro()