# Entrada do usuário
email = input("Informe seu email: ")

# TODO: Verifique as regras do e-mail:
def valid_email(email):
    if '@' in email:
        print("E-mail válido")
    else:
        print("E-mail inválido")
    

