#  classe mãe
class Carro: 
    def __init__(self, motor, rodas):
        self.motor = motor
        self.rodas = rodas

    def acelerar(self): #   self avisa que estou me referindo a classe.
        print("O carro está acelerando! Vrummm-vrummm")

    def frear(self):
        print("O carro está freando, fica esperto!! ")

#   classe Filha herda da classe CARRO
class CarroEsportivo(Carro):
    def __init__(self, motor, rodas, turbo):
        super().__init__(motor, rodas)
        self.turbo = turbo

    def usar_turbo(self):
        if self.turbo:
            print("O carro está ativando o turbo, se segura aí!!! ")
        else:
            print("O carro tá fraquin, turbo indisponível :/ ")

meucarro = CarroEsportivo("V8", 4, True) #  True para o IF verdadeiro. (c/turbo)
print(f"Motor: {meucarro.motor}")
print(f"Rodas: {meucarro.rodas}")
meucarro.acelerar()
meucarro.usar_turbo()
meucarro.frear()

meucarrosturbo = CarroEsportivo("V6", 4, False) #   False para o IF falso. (s/turbo)
meucarrosturbo.usar_turbo()
