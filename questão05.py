hora = int(input("digite um horário: "))
if hora < 0 or hora > 23:
    print("digite um número entre 0 e 23")
else:
    if  4 < hora < 12:
        print("está de manhã")
    elif 11 < hora < 18:
        print("está de tarde")
    else:
        print("está de noite")