def saudacao(nome, mensagem="Olá!"): #Olá é a mensagem padrão que vai aparecer.
    return f'{mensagem}, {nome}!'

print(saudacao("Maria")) 
print(saudacao("João", "Oi")) #se tiver mais um parâmetro, ele vai substituir o segundo parametro (que é a mensagem padrão)
#se não tiver um segundo parâmetro, vai puxar o parametro padrão estabelecido na def.
  
