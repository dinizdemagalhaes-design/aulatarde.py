valor_compra = float(input("Digite o valor da compra: "))
cliente_vip =  input("Digite cliente é VIP ( sim / não): "). lower()

if valor_compra >= 500 or cliente_vip == "sim":
    desconto= 0.10
elif valor_compra >=200 and valor_compra < 500:
    desconto = 0.05
else:
    desconto = 0

valor_desconto = valor_compra * desconto
valor_final = valor_compra - valor_desconto

print("Se o cliente é VIP é:", cliente_vip)
print("Valor da compra é :", valor_compra)
print("Digite o valor do desconto é:", desconto * 100, "%" )
print("Valor do final é:", valor_final)
