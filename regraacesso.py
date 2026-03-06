idade = int(input("Digite a idade: "))
tipo_ingresso = input("Digite o itpo de ingresso (normal /vip: )").lower()

if idade >= 18 and tipo_ingresso == "vip":
    print ("Acesso área VIP")
elif idade >= 18 and tipo_ingresso == "normal":
    print("Acesso área comum")
elif idade >= 16 and idade<= 17 and (tipo_ingresso == "normal" or tipo_ingresso == "vip"):
    print ("Acesso permitido apenas com responsável")
else:
    print("Acesso negado")


print ("Se o cliente e VIP ou Normal é:", tipo_ingresso)
print ("Qual é a sua idade é:", idade)
