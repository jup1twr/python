aluno = input("Digite o seu nome completo: ")
ano = int(input("Digite o ano atual: "))
curso = input("Digite o nome do curso: ")
matriculado_input = input("Você está matriculado? (sim/não) ")

#converter resposta para Bool
#if: se
#else: senão
#matriculado =  True if (se) matriculado_input.lower() (condição)  == "sim" else(senao) False
# elif (outra opções, só se usa quando tem mais 2 condição, como se fosse o "se" dentro do "senao")

if matriculado_input.lower()  =="sim":
    matriculado = True
elif  matriculado_input.lower() =="não" or matriculado_input.lower() == "nao":
    matriculado = False
else:
    matriculado = False
    print("Resposta inválida para matrícula, não matriculado")

if matriculado:
    print(f"{aluno} está matriculado(a) no curso")
else:
    print(f" {aluno} não está matriculado(a) no curso.")
