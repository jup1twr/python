#   crie um programa em python que funcione como uma calculadora básica    #
#   usando funções para cada operação matemática (soma, subtração, multiplicação e divisão)    #
#   o programa deve exibir um menu com as opções de operação para o usuário escolher    #
#   após a seleção, o programa solicitará dois números e em seguida chamará a função correspondente     #
#   para calcular o resultado, que deverá ser exibido ao usuário. programa deve rodar até user out.     #
def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    if b == 0:
        print(f"Divisão por zero não é permitida.")
    return a / b

def menu ():
    print("\n========== CALCULADORA no PYTHON ==========")
    print("0 - Sair")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    input("\nSelecione uma opção: ")
    print("=============================================")
while True: #"enquanto" for verdadeiro:
    menu()
    opcao = ""
    match opcao: #ligue a opção entre
        case "1" | "2" | "3" | "4": #caso 1, 2, 3, 4 (que são as operações matemáticas, a opção de SAIR não entra)
            try: #tente, insirir os números
                numero1 = float(input("Digite o primeiro número: "))
                numero2 = float(input("Digite o segundo número: "))
            except ValueError: #exceção, se não for inserido da forma solicitada
                print("Erro: Digite um número válido.")
                continue #para continuar o código até que insira de forma correta
            match opcao: #ligue a opcao aos casos 0, 1, 2, 3 e 4
                case "1":
                    resultado = soma(numero1,numero2)
                case "2":
                    resultado = subtracao(numero1, numero2)
                case "3":
                    resultado = multiplicacao(numero1, numero2)
                case "4":
                    resultado = divisao(numero1, numero2)
            print(f"Resultado: {resultado}")
        case "0":
            print("Programa Encerrado.")
            break #parar o programa "quebrar"
        case _: #caso não for nenhuma das opções, exibir isso
            print("Opção Inválida! Por favor, selecione uma opção entre 0 e 4.")
        
            