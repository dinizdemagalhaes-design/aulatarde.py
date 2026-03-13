saldo = 1000
senha_sistema = "1234"

continuar = "s"

while continuar == "s":

    valor = float(input("Digite o valor do saque: "))
    senha = input("Digite sua senha: ")

    if senha != senha_sistema:
        print("Senha incorreta. Operação cancelada.")

    elif valor <= 0:
        print("Valor inválido para saque.")

    elif valor > 500:
        print("Valor excede o limite permitido por operação.")

    elif valor > saldo:
        print("Saldo insuficiente para realizar o saque.")

    else:
        saldo -= valor
        print("Saque realizado com sucesso.")
        print("Novo saldo:", saldo)

    continuar = input("Deseja realizar outra operação? (s/n): ")

print("Sistema encerrado. Obrigado por utilizar o caixa eletrônico.")
