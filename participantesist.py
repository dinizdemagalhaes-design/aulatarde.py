idade = int(input("Digite a idade do participante: "))
tipo_ingresso = input("Tipo de ingresso (normal, vip, premium: )").lower()
anos_experiencia = int(input("Tempo de experiência: "))

if idade >= 18 and tipo_ingresso == "premium" and anos_experiencia >=3:
    print ("Acesso Premium liberado: todas as áreas disponíveis")
elif idade >= 18 and tipo_ingresso == "vip":
    print ("Acesso VIP liberado")
elif idade == 16 and idade == 17 and (tipo_ingresso =="vip" or tipo_ingresso == "premium"):
    print ("Acesso limitado: menores não podem acessar áreas VIP ou Premium")
else:
    print ("Acesso negado")
