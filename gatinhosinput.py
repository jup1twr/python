class Gato:
    def __init__(self, raca, nome, peso, idade):
        self.raca = raca
        self.nome = nome
        self.peso = peso
        self.idade = idade
    def mostrardados(self):
        print(f"Raça: {self.raca}")
        print(f"Nome: {self.nome}")
        print(f"Peso: {self.peso}")
        print(f"Idade: {self.idade} anos")
#   solicitar dados ao user
raca = input("Insira a raça do gato: ")
nome = input("Insira o nome do gato: ")
peso = float(input("Insira o peso do gato: (em kg)"))
idade = int(input("Insira a idade do gato: (em anos)"))