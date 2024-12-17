import re

def verificar_forca_senha(senha):
    result = {}  # Dicionário para armazenar os resultados

    pat = re.compile(r'[^a-zA-Z0-9]')
    comprimento_minimo = 8
    tem_letra_maiuscula = False
    tem_letra_minuscula = False
    tem_numero = False
    tem_caractere_especial = False

    if len(senha) < comprimento_minimo:
        print("Sua senha é muito curta. Recomenda-se no mínimo 8 caracteres.")
        return

    # Verificando se a senha contém sequências comuns
    sequencias_comuns = ["123456", "abcdef"]
    palavras_comuns = ["password", "123456", "qwerty"]
    if senha in sequencias_comuns:
        print("Sua senha contém uma sequência comum. Tente uma senha mais complexa.")
        return
    elif senha in palavras_comuns:
        print("Sua senha é muito comum. Tente uma senha mais complexa.")
        return

    # Verificar se a senha contém caractere especial
    if pat.search(senha):
        tem_caractere_especial = True
    result["Caractere_Especial"] = tem_caractere_especial

    # Verificar o comprimento da senha
    if len(senha) >= comprimento_minimo:
        result["Comprimento"] = True
    else:
        result["Comprimento"] = False

    # Verificar letras maiúsculas e minúsculas
    for i in senha:
        if i.isupper():
            tem_letra_maiuscula = True
        if i.islower():
            tem_letra_minuscula = True
    result["Maiuscula"] = tem_letra_maiuscula
    result["Minuscula"] = tem_letra_minuscula

    # Verificar se a senha contém números
    for i in senha:
        if i.isdigit():
            tem_numero = True
    result["Numero"] = tem_numero

    # Verificar se todos os critérios foram atendidos
    if all(result.values()):
        print("Sua senha atende aos requisitos de segurança. Parabéns!")
    else:
        print("Sua senha não atende aos requisitos de segurança.")

# Obtendo a senha do usuário
senha = input().strip()

# Verificar a força da senha
verificar_forca_senha(senha)