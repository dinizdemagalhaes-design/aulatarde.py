saldo = 1000
senha = "1234"
continuar = "s"

while continuar =="s":
    opcao = input("Digite 1 para saque ou 2 para depósito: ")
    tentativas = 0
    while tentativas < 3:
        senha_digitada = input("Digite a senha")
        if senha_digitada == senha:
            break
        else:
            tentativas += 1
            print("Senha incorreta")
    if tentativas == 3:
        print("3 tentativas incorretas. Operação cancelada")
    else:
        valor = float(input("Digite o valor do saque: "))
        if valor <= 0:
            print("Valor inválido para saque.")
        elif opcao == "1":
            if valor > 500:
                print("Valor excede o limite permitido por operação.")
            elif valor > saldo:
                print("Saldo insuficiente para realizar o saque") 
            else:
                saldo -= valor
            print ("Saque realizado com sucesso.")
            print ("Novo saldo: ", saldo)
        elif opcao == "2":
            saldo += valor
            print ("Depósito realizado com sucesso")
            print ("Novo saldo: ", saldo)
        else:
            print("Opção inválida")
                      





    continuar = input("Deseja realizer outra operação? (s/n): ")
print ("Sistema encerrado. Obrigado por utilizar o caixa eletrônico.")
