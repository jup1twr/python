idade = int(input())
#idade é em dias
ano = idade // 365
diasrest = idade % 365
meses = diasrest // 30
dias = diasrest % 30
print(f"{ano} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
