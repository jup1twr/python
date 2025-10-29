#   desenvolva um programa em python que implemente um sistema simples 
#   de cadastro de alunos utilizando somente funções (def). o programa deve incluir:
#   uma função para cadastrar o aluno, que receba uma lista e os dados do aluno (nome, idade, curso)
#   e adicione essas informações como um dicionário a lista;
#   e uma função que liste todos os alunos cadastrados, exibindo seus dados de forma organizada.
#   teste o sistema cadastrando alguns alunos e exibindo a lista ao final
#    *sem utilizar classe, apenas estruturas básicas.

def cadastraralunos(lista, nome, idade, curso):
    aluno ={"nome": nome, "idade": idade, "curso": curso}
    lista.append(aluno) #   adicionar o aluno a lista
def listaraluno(lista):
    for i in range(len(lista)): #len (length) = comprimento
        aluno = lista[i]
        print(f"{i + 1}. Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}")
alunos = []

while True:
    print("Cadastro de Aluno")
    nome = input("Nome completo (ou sair para encerrar): ")
    if nome.lower() == "sair": #    se o "nome" for == a sair, em caps lock ou minusculo
        break # para encerrar o programa
    idade = int(input("Idade: "))
    curso = input("Curso: ")
    cadastraralunos(alunos, nome, idade, curso)
    print("Aluno cadastrado com sucesso! \n")
print("\n Lista de alunos cadastrado: ")
listaraluno(alunos)
