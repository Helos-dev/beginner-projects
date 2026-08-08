#CLASS DEFINITION
class Animal:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    def mangia(self):
        print(f"{self.nome} sta mangiando")
    def faiverso(self):
        print (f"{self.nome} abbaia")
class Cane(Animal):
    def __init__(self, nome, eta, razza):
        super().__init__(nome, eta)
        self.razza = razza
    def faiverso(self):
        print("Bau Bau")
class Gatto(Animal):
    def __init__(self, nome, eta):
        super(). __init__(nome, eta)
    def faiverso(self):
        print("Miao Miao")
class Uccello(Animal):
    def __init__(self, nome, eta, ):
        super().__init__(nome, eta)
    def faiverso(self):
        print("Cip Cip")

#TEST
cane1 = Cane("Bobby", 3, "Labrador")
cane1.mangia()
cane1.faiverso()

Uccello1 = Uccello("Titty", 1)
Uccello1.faiverso()
Uccello1.mangia()