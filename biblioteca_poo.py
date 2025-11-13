#   crie um programa em python que simule um sistema de bibliotea utilizando conceitos
#   de programação orientada a objetos. o sistema deve: definir uma classe Livro que
#   contenha, pelo menos, os atributos: titulo (nome do livro), autor (nome do autor)
#   criar uma lista com pelo menos 10 objetos Livro, representando os livros disponíveis
#   solicitar ao user o nome do solicitante do empréstimo, exibir a lista de livros
#   numerada para facilitar a seleção, pedir ao usuário escolher um número correspondente
#   ao livro que deseja. por fim, imprimir uma mensagem informando o nome do solicitante e o livro selecionado.

class Livro:
    def __init__(self, titulo, autor): #    self refere a própria função, ou seja, a oq a própria funãção vai atribuir
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.livros = [
            Livro("Diário de um Banana, vol. I", "Jeff Kinney"),
            Livro("Diário de um Banana, vol. II", "Jeff Kinney"),
            Livro("Diário de um Banana, vol. III", "Jeff Kinney"),
            Livro("Bom dia, Verônica", "Raphael Montes"),
            Livro("todas as coisas que eu te escreveria se pudesse", "Igor Pires"),
            Livro("Água-viva", "Clarice Lispector"),
            Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry"),
            Livro("Heartstopper", "Alice Oseman"),
            Livro("Uma Família Feliz", "Raphael Montes"),
            Livro("o fim em doses homeopáticas - textos crueis demais", "Igor Pires"), #    esses são os objetos da lista
                    ]
        
    def exibir_livros(self):
        print("\n=============== LIVROS DISPONÍVEIS ===============")
        for i, livro in enumerate(self.livros, 1): #    para contador, livro em enumarar (self.livros), começando do nº1
            print(f"{i}. '{livro.titulo}' por {livro.autor}")  #    printar o Nº, o título e o autor
    
    def solicitar_emprestimo(self):
        solicitante = input("\nDigite seu nome: ").strip() #    strip para tirar os espaços desnecessários
        self.exibir_livros()
        try: #  tente:
            escolha = int(input(f"\n{solicitante}, escolha o número do livro: ")) #     escolha é a variável para escolher o Nº do livro
            if 1 <= escolha <= len(self.livros): #  len é para medir, comprimento, ele vê se a escolha vai ser compatível com o tamanho da lista
                livro_escolhido = self.livros[escolha - 1] #    ou seja, n vai poder escolher o livro que foi emprestado
            
                print(f"\n=============== EMPRÉSTIMO REALIZADO ===============")
                print(f"Solicitante: {solicitante}")
                print(f"Livro: '{livro_escolhido.titulo}' por {livro_escolhido.autor}")
            else:
                print("Número inválido!")
        
        except ValueError:
            print("Digite apenas números!")

sistema = Biblioteca()
sistema.solicitar_emprestimo()

