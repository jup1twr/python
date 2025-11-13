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
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def fazersom(self): #   para sobrescrever, tem que usar o mesmo nome da função
        if self.fazersom:
            print("O gatinho tá miando! Miawwww!")
        else: 
            print("O animal fez um som!")

print("====================================================")
animal = Animal("Cleitin", 5)
print(f"Nome: {animal.nome}, Idade: {animal.idade} anos")
animal.fazersom()
print("====================================================")

cachorro = Cachorro("Spike", 2)
print(f"Nome: {cachorro.nome}, Idade: {cachorro.idade} anos")
cachorro.fazersom()
print("====================================================")

gato = Gato("Capitão", 3)
print(f"Nome: {gato.nome}, Idade: {gato.idade} anos")
gato.fazersom()
print("====================================================")