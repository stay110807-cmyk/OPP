#Example 1
class Animal:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def comer(self):
        print(self.nombre, "Esta comiendo")

    def caracteristica(self):
        print(self.nombre, "es raza: ", self.raza)

class Perro(Animal):
    def ladrar(self):
        print(self.nombre, "Esta ladrando")


perro = Perro("Firulais", "Pitbull")

perro.comer()
perro.ladrar()
perro.caracteristica()

class Gato(Animal):
    def maullar(self):
        print(self.nombre, "Esta maullando")
    
    def cazar(self):
        print(self.nombre, "Esta consiguiendo comida")

gato=Gato("Garfield", "Gato montes")
gato.maullar()
gato.cazar()
gato.caracteristica()