#   desenvolva um programa em python que implemente um sistema simples 
#   de cadastro de alunos utilizando somente funções (def). o programa deve incluir:
#   uma função para cadastrar o aluno, que receba uma lista e os dados do aluno (nome, idade, curso)
#   e adicione essas informações como um dicionário a lista;
#   e uma função que liste todos os alunos cadastrados, exibindo seus dados de forma organizada.
#   teste o sistema cadastrando alguns alunos e exibindo a lista ao final
#    *sem utilizar classe, apenas estruturas básicas.
alunocadastrado = []
opcao = ""
#   \n para pular linhas

def cadastroaluno(lista):
    print("===================== CADASTRAR o ALUNO =====================")
    nome = input("Insira o nome completo do aluno: ") 
    idade = int(input("Insira a idade do aluno: "))
    curso = input("Insira o curso que deseja matricular o aluno: ")
    aluno = {"nome": nome, "idade": idade, "curso": curso} #    dicionário, liga as variáveis aos inputs
    lista.append(aluno) # .append(), adiciona o item na lista.
    print(f"Aluno(a) '{nome}' cadastrado com sucesso!")

def listaalunos(lista):
    print("\n=================== LISTA DE ALUNOS ===================")
    if not lista: # Verifica se a lista está vazia
        print("Nenhum aluno cadastrado.")
        return
    for i in range(len(lista)):
        aluno = lista[i]
        #   usa f-string para exibir os dados de forma organizada
        print(f"[{i + 1}] | Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}") #   puxa os dados do dicionário de antes

while True:
    opcao != "0"
    print("\n========== SISTEMA de ALUNOS ==========")
    print("0 - Sair")
    print("1 - Cadastrar aluno")
    print("2 - Lista de alunos cadastrados")
    opcao = input("\nSelecione uma opção: ")
    if opcao == "1":
        cadastroaluno(alunocadastrado)
    elif opcao == "2":
        listaalunos(alunocadastrado)
    elif opcao == "0":
        print("Você está saindo do Sistema de Alunos. Até mais!")
    else:
        print("Opção inválida! Por favor, escolha uma opção entre 0 e 2.")