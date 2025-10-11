nome = input ("Digite o seu nome: ")
#input guarda as informações como se fossem strings(caracteres)
idade = int(input ("Digite sua idade: "))
#int converte para número inteiro
altura = float(input ("Digite a sua altura: "))
#float converte para número real 

#print("Nome: " + nome + ", Idade: " + str(idade) +",Altura: " +str(altura)) -- método 1 de converter para string
#print("Nome: ", nome, ", Idade: ", idade +",Altura: ", altura) #método 2 de converter para string

print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}") 
      
#método 3 de converter para string (mais recomendado e mais fácil)
#print associa a variável a entrada de dados insirida pelo user