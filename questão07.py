aluno = input("digite o nome do aluno: ")
dicip = input("digite o nome matéria: ")
nota1 = float(input("digite a nota parcial: "))
nota2 = float(input("digite a nota bimestral: "))
media = ((nota1 + nota2) / 2)
if media < 6:
   status = (f'reprovado')
else:
    status = (f'aprovado')
print(f'{aluno} está {status} na disciplina {dicip}')
