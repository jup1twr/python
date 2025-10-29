#   crie um programa que inclua uma função chamada SomaImposto
#   essa função deve receber DOIS parâmetros:
#   TaxaImposto: que representa a porcentagem do imposto sobre vendas
#   Custo: que é o valor do item antes da aplicação do imposto.
#   a função deve calcular o valor do imposto A PARTIR da taxa fornecida
#   e adicionar esse valor ao custo inicial, retornando o novo custo com o imposto incluído.
def SomaImposto(): #    se for usar input, não coloque nada dentro dos parenteses; se usar, precisa dos parametros
    TaxaImposto = float(input('Insira a taxa de imposto a se considerar: '))
    Custo = float(input('Insira o custo do item: '))
    ValorImposto = (TaxaImposto/100) * Custo
    CustoTotal = ValorImposto + Custo
    return f"{CustoTotal:.2f}"
print(SomaImposto()) #  chama a função e dá o resultado, precisa de print(nomedafuncao())
