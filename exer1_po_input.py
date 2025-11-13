#   crie uma classe animal com os atributos nome e idade.
#   crie um método fazer som() que imprime uma msg genérica.
#   crie duas classes filhas, cachorro e gato, que herdam de animal.
#   sobrescreva o método fazer som nas classes filhas para imprimir.
#   sons específicos (auau para dog, miau para cat)

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def fazersom(self):
        print(f"O animal está fazendo um barulho! Escute com atenção!")

class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def fazersom(self):
        if self.fazersom:
            print("O cachorrinho tá latindo! Au-Auuu!")
        else:
            print("O animal fez um som!")

class Gato(Animal):
    def __init__(self, nome, idade,):
        super().__init__(nome, idade)

    def fazersom(self): #   para sobrescrever, tem que usar o mesmo nome da função
        if self.fazersom:
            print("O gatinho tá miando! Miawwww!")
        else: 
            print("O animal fez um som!")

nome = input("Digite o nome do animal: ")
idade = float(input("Digite a idade do animal (em anos): "))
tipo = input("Digite o tipo do animal (animal, cachorro ou gato): ").strip().lower()

if tipo == "cachorro":
    animal = Cachorro(nome,idade)
elif tipo == "gato":
    animal = Gato(nome,idade)
else:
    animal = Animal(nome,idade)

animal.fazersom()

