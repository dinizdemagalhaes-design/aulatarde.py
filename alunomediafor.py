quantidade_alunos = int(input("Qual a quantidade de alunos avaliados: "))

aprovados = 0
recuperacao = 0
reprovados = 0

for aluno in range (1, quantidade_alunos+1):
    print("\nAluno", aluno)
    nota1 = float(input("Nota 1:"))
    nota2 = float(input("Nota 2:"))
    
    media = (nota1 + nota2) /2
    print = ("Média", media)
    
    if media >= 7:
        print ("Aprovado")
        aprovados += 1

    elif media >= 5:
        print ("Recuperação")
        recuperacao += 1
        
    else:
        print ("Reprovado")
        reprovados += 1
    


print ("o numero de alunos aprovados é:", aprovados)
print ("O número de alunos em recuperação é:", recuperacao)
print ("O numero de alunos reprovados é", reprovados)
