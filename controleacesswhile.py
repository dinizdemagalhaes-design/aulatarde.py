autorizada = 0
recusada = 0

continuar = "s"

while continuar =="s":
    nome = str(input(" Digite seu nome: ")).lower()
    idade = int(input("Digite a idade: "))
    credencial = str(input("Digite o tipo de credencial(vip/ normal / nenhuma): "))
    
    if idade >= 18 and (credencial == "vip" or credencial == "normal"): 
        print("Entrada permitida")
        autorizada += 1
    else:
        ("Entrada negada") 
        recusada += 1

    continuar = input("Deseja registar outra entrada? (s/n):")


print("\n Sistema encerrado")
print("Total de pessoas autorizadas:", autorizada)
print("Total de pessoas recusadas:", recusada)

