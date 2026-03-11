numero = int(input("Digite um número inteiro: "))
             
i = 1
while i <= 10:
    for i in range (1, 11):
        resultado = numero * i 
        print (f'{numero} X {i} = {resultado}')
    break    
