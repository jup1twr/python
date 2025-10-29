print("*" *35)
print("Bem-vindo(a) ao Jogo da Forca!")
print("*" *35) #repete o * asterisco 35x

palavrasecreta = "laranja"
letrasacertadas = ['_','_','_','_','_','_','_',]

enforcou = False
acertou = False
erros = 0

while(not acertou and not enforcou):
    chute = input("Qual letra quer adicionar? ")
    
    if (chute in palavrasecreta):
        posicao = 0
        for letra in palavrasecreta:
            if(chute.upper() == letra.upper()):
                letrasacertadas[posicao] = letra
            posicao = posicao + 1
    else:
        erros += 1
    enforcou == erros == 7 #se o n de erros for igual 7, igual True
    acertou = "_" not in letrasacertadas
    print(letrasacertadas)
if acertou:
    print("Você ganhou!!!")
    print(f"A palavra-secreta era: {palavrasecreta}")
    print("*" *35)
    print("Fim do Jogo da Forca")
    print("*" *35)
else:
    print("Você perdeu!!!")
    print("*" *35)
    print("Fim do Jogo da Forca")
    print("*" *35)      