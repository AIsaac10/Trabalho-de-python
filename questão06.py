cid = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
if idade < 16:
    print(f'{cid} você não tem idade para retirar o titulo de eleitor')
else:
    print(f'{cid}, você tem {idade} anos e já pode retirar o titulo de eleitor')