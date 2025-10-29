#elabore um programa que receba o nome do dia da semana
#fim de semana se for sábado ou domingo
#início da semana se for segunda-feira
#dia útil para os outros dias

#lower é para deixar tudo minusculo
#strip é para tirar os espaços em excesso no inicio e no fim

dia = input ("Qual é o dia da semana?").strip().lower()

if dia == "sábado" or dia == "domingo" or dia == "sabado":
    print("Fim de semana, descansa CLT!")
elif dia == "segunda-feira" or dia == "segunda":
    print("Início da semana, chora CLT!")
elif dia == "terça-feira" or dia == "terça" or dia == "quarta-feira" or dia == "quarta" or dia =="quinta-feira" or dia == "quinta":
    print("Dia útil, tá quase lá CLT!")
elif dia =="sexta-feira" or dia == "sextou" or dia == "sexta":
    print("Comemora, Sextou CLT!")
else:
    print("Dia inválido")