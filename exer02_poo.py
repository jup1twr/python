#   implemente a classe Aluno com atributos nome, matrícula e notas (lista),
#   métodos para adicionar nota validando entre 0 e 10, calcular média
#   retornar situação ("Aprovado", "Recuperação" ou "Reprovado")
#   conforme média e listar todas as notas.

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []  #  lista vazia para armazenar as notas

    def adicionarnota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
            return "Nota adicionada com sucesso!"
        else:
            return "Nota inválida. Insira uma nota de 0 a 10."

    def calcularmedia(self):
        if not self.notas:  # se a lista estiver vazia
            return 0
        total = 0
        quantidade = 0
        for nota in self.notas:
            total += nota
            quantidade += 1
        return total / quantidade
    
    def situacao(self):
        media = self.calcularmedia()
        if media >= 7:
            return "Você foi aprovado(a). Parabéns!!!"
        elif media >= 5:
            return "Você está de recuperação. Recupera essa nota aí!!!"
        else:
            return "Você foi reprovado. Até ano que vem!!!"
    
    def listarnotas(self):
        return self.notas

nome = input("Insira seu nome: ")
matricula = int(input("Insira sua matrícula: "))

aluno = Aluno(nome, matricula)

#   adicionando as 4 notas:
for i in range(4):
    while True: #   enquanto for verdadeiro
        try: #  tente
            nota = float(input(f"Insira sua {i+1}ª nota: "))
            resultado = aluno.adicionarnota(nota)
            print(resultado)
            if "sucesso" in resultado:
                break # quebra para encerrar aqui
        except ValueError: #    uma exceção
            print("Por favor, insira um número válido.")

#   mostrando os resultados (FINALMENTE)

print(f"\n========= Resultado Final =========")
print(f"Aluno(a): {aluno.nome}")
print(f"Matrícula: {aluno.matricula}")
print(f"Suas notas foram: {aluno.listarnotas()}")
print(f"Sua média foi: {aluno.calcularmedia():.1f}")
print(aluno.situacao())