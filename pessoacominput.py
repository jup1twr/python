class Pessoa:
    def __init__ (self,nome,idade): #   init = construtor, inicializa os atributos ao criar o objeto
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
#   criando objetos (instância) da classe Pessoa
pessoa1 = Pessoa("Ana", 25)
pessoa2 = Pessoa("The Weeknd", 19)

#   usando os objetos
pessoa1.apresentar()
pessoa2.apresentar()