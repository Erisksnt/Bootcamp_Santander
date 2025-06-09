# Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:
def valid_email():
    if '@' and ' ' in email:
        return("E-mail válido")
    else:
        return("E-mail inválido")