import math


class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Rectangulo")
        #self.nombre = __class__.__name__
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def __str__(self):
        return f'{self.nombre} [base:{self.base} altura:{self.altura}]'

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Circulo")
    #def __init__(self, nombre, radio):
        #self.nombre = __class__.__name__
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio
    
    def __str__(self):
        return f'{self.nombre} [radio:{self.radio}]'
    
def probar_figura(figura):
    print("Estado del objeto:")
    print(figura)
    try:
        print("Área de la figura: ", figura.area())
        print("Perímetro de la figura: ", figura.perimetro())
    except AttributeError:
        print("Error: la figura no tiene definidos los metodos de cálculo de área y perimetro.")
