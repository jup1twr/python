class Pessoa:
    def __init__ (self): #   init = construtor, inicializa os atributos ao criar o objeto
        self.nome = input("Digite o seu nome: ")
        self.idade = int(input("Digite a sua idade: "))
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
#   criando objetos (instância) da classe Pessoa
pessoa1 = Pessoa()

#   usando os objetos
pessoa1.apresentar()
