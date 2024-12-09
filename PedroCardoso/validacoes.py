# VALIDAÇÃO DE EMAIL -------------------------------------------
# # Função
def validar_numero():
    while True:
        entrada = input("Digite um número entre 1 e 10: ")
        if entrada.isdigit(): # ---> Verificar se o input é um digito
            numero = int(entrada)
            if 1 <= numero <= 10:
                print(f"Número válido: {numero}")
                return numero
            else:
                print("Erro: O número deve estar entre 1 e 10")
        else:
            print("Erro: Entrada inválida. Digite um número inteiro.")
# Chamar função
validar_numero()

# VALIDAÇÃO DE INPUT ESTAR EM LISTA -------------------------------------------
# Função
def validar_marca():
    marcas_validas = {"Toyota", "Honda", "Ford", "Tesla"}
    while True:
        entrada = input("Insira uma marca de carro válida (Toyota, Honda, Ford, Tesla)")
        if entrada.isalpha(): # ---> Verificar se o input é um alfanúmerico
            if entrada in marcas_validas: # ---> Verificar se o valor do input está na lista
                print(f"Marca válida: {entrada}")
                return entrada
            else:
                print("Erro: A marca não está na lista de marcas válidas.")
        else:
            print("Erro: Entrada inválida. Digite apenas texto.")
# Chamar função
validar_marca()

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