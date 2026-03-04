nota_final = float(input("Digite a nota final do aluno : "))
frequencia = float(input ("Digite a frequencia do aluno em (%): "))


if nota_final >=7 and frequencia >= 75:
    print("O aluno está aprovado e pode participar do torneio")
elif nota_final >= 6 and frequencia >= 70:
    print("O aluno não cumpriu todos os requisitos, mas está autorizado a participar")
else:
    print ("O aluno não está autorizado a participar do torneio")
