#   crie um programa em python que simule um sistema de bibliotea utilizando conceitos
#   de programação orientada a objetos. o sistema deve: definir uma classe Livro que
#   contenha, pelo menos, os atributos: titulo (nome do livro), autor (nome do autor)
#   criar uma lista com pelo menos 10 objetos Livro, representando os livros disponíveis
#   solicitar ao user o nome do solicitante do empréstimo, exibir a lista de livros
#   numerada para facilitar a seleção, pedir ao usuário escolher um número correspondente
#   ao livro que deseja. por fim, imprimir uma mensagem informando o nome do solicitante e o livro selecionado.
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

def main():
    livros = [
        Livro("Diário de um Banana, vol. I", "Jeff Kinney"),
        Livro("Diário de um Banana, vol. II", "Jeff Kinney"),
        Livro("Diário de um Banana, vol. III", "Jeff Kinney"),
        Livro("Bom dia, Verônica", "Raphael Montes"),
        Livro("todas as coisas que eu te escreveria se pudesse", "Igor Pires"),
        Livro("Água-viva", "Clarice Lispector"),
        Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry"),
        Livro("Heartstopper", "Alice Oseman"),
        Livro("Uma Família Feliz", "Raphael Montes"),
        Livro("o fim em doses homeopáticas - textos crueis demais", "Igor Pires"),
            ]
    
    nome = input("Digite seu nome: ")

    print("\nLivros disponíveis para empréstimo:\n")
    for i, livro in enumerate(livros, start=1):
        print(f"{i}. {livro.titulo} por {livro.autor}")

    while True:
        try:
            escolha = int(input("\nDigite o número do livro que deseja pegar emprestado: "))
            if 1 <= escolha <= len(livros):
                livroselect = livros[escolha - 1]
                print(f"\nEmpréstimo confirmado!")
                print(f"{nome} pegou emprestado o livro '{livroselect.titulo}' de {livroselect.autor}")
                break
            else:
                print(f"Por favor, selecione um número entre 1 e {len(livros)}")
        except ValueError:
            print("Por favor, digite um número válido.")

main()