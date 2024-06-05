hora = int(input("digite um horário: "))
if hora < 0 or hora > 23:
    print("digite um número entre 0 e 23")
else:
    if  0 <= hora <= 11:
        print("está de manhã")
    elif 12 <= hora <= 17:
        print("está de tarde")
    else:
        print("está de noite")
