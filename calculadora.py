#   crie um programa em python que funcione como uma calculadora básica    #
#   usando funções para cada operação matemática (soma, subtração, multiplicação e divisão)    #
#   o programa deve exibir um menu com as opções de operação para o usuário escolher    #
#   após a seleção, o programa solicitará dois números e em seguida chamará a função correspondente     #
#   para calcular o resultado, que deverá ser exibido ao usuário. programa deve rodar até user out.     #

opcao = ""

def soma_input():
    n1 = int(input('Insira um número: '))
    n2 = int(input('Insira um número: '))
    result = n1 + n2
    return result

def subtracao_input():
    n1 = int(input('Insira um número: '))
    n2 = int(input('Insira um número: '))
    result = n1 - n2
    return result

def multiplicacao_input():
    n1 = int(input('Insira um número: '))
    n2 = int(input('Insira um número: '))
    result = n1 * n2
    return result

def divisao_input():
    n1 = int(input('Insira um número: '))
    n2 = int(input('Insira um número: '))
    if n2 == 0:
        print(f"Divisão por zero não é permitida.")
        return None
    result = n1 // n2
    return result

opcao = ""

while opcao != "0":
    print("\n========== CALCULADORA no PYTHON ==========")
    print("0 - Sair")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    
    opcao = input("\nSelecione uma opção: ")
    
    if opcao == "1":
        result = soma_input()
        if result is not None:
            print(f"O resultado da soma é: {result}")
    
    elif opcao == "2":
        result = subtracao_input()
        if result is not None:
            print(f"O resultado da subtração é: {result}")
    
    elif opcao == "3":
        result = multiplicacao_input()
        if result is not None:
            print(f"O resultado da multiplicação é: {result}")
    
    elif opcao == "4":
        result = divisao_input()
        if result is not None:
            print(f"O resultado da divisão é: {result}")
    
    elif opcao == "0":
        print("Você está saindo da Calculadora. Até mais!")
    
    else:
        print("Opção inválida! Por favor, escolha uma opção entre 0 e 4.")
print("Programa encerrado.")
    