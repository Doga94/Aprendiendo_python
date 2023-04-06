class Person(object):
    def __init__(self, nombre):
        self.nombre = nombre

    def saltar(self):
        print(f'{self.nombre} Salta muy bajo')

class Constructor(Person):
    def saltar(self):
        print(f'{self.nombre} No salta mucho')

class Jugador(Person):
    def saltar(self):
        print(f'{self.nombre} Salta 2 metros')