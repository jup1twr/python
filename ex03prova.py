def dia_da_semana(numero):
    match numero:
        case 1:
            print(f"Segunda-feira")
        case 2:
            print(f"Terça-feira")
        case 3:
            print(f"Quarta-feira")
        case 4:
            print(f"Quinta-feira")
        case 5:
            print(f"Sexta-feira")
        case 6:
            print(f"Sábado")
        case 7:
            print(f"Domingo")
        case _:
            print("Dia inválido")
    
