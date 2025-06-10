# Entrada do usuário
email = input("Informe seu email: ")

# TODO: Verifique as regras do e-mail:

def validar_email(email):
    if '@' in email and '.' in email:  # Primeiro verifica se existem ambos caracteres
        if email.index('@') > 0 and email.index('.') > email.index('@') + 1:
            return True
    return False
    
if validar_email(email):
    print("E-mail válido")
else:
    print("E-mail inválido")

    

