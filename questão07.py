aluno = input("digite o nome do aluno: ")
dicip = input("digite o nome matéria: ")
nota1 = float(input("digite a nota parcial: "))
nota2 = float(input("digite a nota bimestral: "))
media = ((nota1 + nota2) / 2)
if media < 6:
    print(f'O aluno {aluno} está "reprovado" na matéria {dicip} com média {media}')
else:
    print(f'O aluno {aluno} está "aprovado" na matéria {dicip} com média {media}')