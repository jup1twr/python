class Carro:
    def acelerar(self):
        print(f"O carro tá acelerando normal.")

class CarroEsportivo(Carro):
    def acelerar(self):
        print("O carro tá acelerando D+!!")

#   criando objetos
carrocomum = Carro()
carroesportivo = CarroEsportivo()

#   chamando métodos
carrocomum.acelerar()
carroesportivo.acelerar()