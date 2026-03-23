lista = []

while True:
    print("\n====== Lista de Compras======")
    print("[i] Inserir um item")
    print("[a] Apagar item")
    print ("[l] Listar item")
    print("[s] Sair do sistema")

    opção = input("Escolha uma opção: ").lower()
   
    if opção == "i":
        item = input("Digite o item:")
        lista.append(item)
        print("Item adicionado com sucesso")  

    elif opção=="a":
        try:
            if not lista:
                print("A lista está vazia.")
            else:
                for i, item in enumerate(lista):
                    print(i, "-", item)
                
                indice =int(input("Digite o índice do item: "))
                removido = lista.pop(indice)
                print(f"item '{removido} removido!")
        
        except ValueError:
            print("Digito um numero invalido")
        except IndexError:
            print("Indice não existe")

    elif opção == "l":
        if not lista:
            print(("A lista esta vazia"))
        
        else:
            print("Itens da lista:")
            for i, item in enumerate(lista):
                print(i, "-", item)

    elif opção == "s":
        print("Sair do Sistema")
        break
    
    else:
        print("Opção inválida")
