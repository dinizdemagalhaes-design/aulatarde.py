numeros = (5, 8, 0, 12, 7, 3, 10, 4, 9, 6)
pares = 0
impares = 0

for numero in numeros:
    if numero == 0:
        print ("Encontrado o número zero")
    elif numero %2 ==0 :
        pares += 1
    else:
        impares += 1
    
print ("A quantidade de pares é:", pares )
print ("A quantidade de ímpares é:", impares)
