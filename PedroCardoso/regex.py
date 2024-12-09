# VALIDAÇÃO DE EMAIL ------------------------------------------- 
import re # --> Importar biblioteca de regex (regular expressions)
# Função
def validar_email():
    while True:
        email = input("Digite um email: ")
        # Regex para validação básica de email
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(padrao, email):
            print(f"Email válido: {email}")
            return email
        else:
            print("Erro: Email inválido. Tente novamente")
# Chamar função
validar_email()
