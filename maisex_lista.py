tarefas = [] #  lista vazia, para receber dados

while True:
    print("\n--- MINHAS TAREFAS ---")
    print("1. Ver tarefas")
    print("2. Adicionar tarefa")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        if not tarefas:
            print("Nenhuma tarefa na lista!")
        else:
            print("\nSuas tarefas:")
            for i, tarefa in enumerate(tarefas, 1):
                print(f"{i}. {tarefa}")
    
    elif opcao == "2":
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas.append(nova_tarefa)
        print(f"Tarefa '{nova_tarefa}' adicionada!")
    
    elif opcao == "3":
        print("Até logo!")
        break
    
    else:
        print("Opção inválida!")