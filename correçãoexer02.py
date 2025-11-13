#   implemente a classe Aluno com atributos nome, matrícula e notas (lista),
#   métodos para adicionar nota validando entre 0 e 10, calcular média
#   retornar situação ("Aprovado", "Recuperação" ou "Reprovado")
#   conforme média e listar todas as notas.

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionarnota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
    
    def calcularmedia(self):
        return sum(self.notas)/len(self.notas) if self.notas else 0 #   sum para somar, len para juntar tudo
    
    def mostrarresultado(self):
        media = self.calcularmedia()
    
    def listarnotas(self):
        return self.notas

nome = input("Nome: ")
matricula =  input("Matrícula: ")
aluno = Aluno(nome, matricula)

while True:
    nota = input("Nota (ou enter para sair): ")
    if nota == "":
        break
    try:
        aluno.adicionarnota(float(nota))
    except:
        print("Insira um número válido!")

print(f"Notas: {aluno.listarnotas()}")
print(f"Média: {aluno.calcularmedia():.2f}")
print(f"Resultado: {aluno.mostrarresultado()}")
