verificacao = {}


def senha(password):

    digito = False

    if len(password) >= 8:
        verificacao["Tamanho"] = True
    else:
        verificacao["Tamanho"] = False

    for item in password:
        if item.isdigit():
            digito = True
    verificacao["Numeral"] = digito   
    for item in password:
        if item.isupper():
            digito = True
    verificacao["Maiuscula"] = digito

    if all(verificacao.values()):
        print("Strong")
    else:
        print("Weak")

senha(input("Digite: "))    




