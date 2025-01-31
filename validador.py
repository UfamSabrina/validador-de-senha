import string

def validar_tamanho(senha): #Tamanho
    return len(senha) >= 8

def validar_numero(senha): #Número
    return any(c.isdigit() for c in senha)

def validar_minuscula(senha): #Minúsculo
    return any(c.islower() for c in senha)

def validar_maiuscula(senha): #Maiúsculo
    return any(c.isupper() for c in senha)

def validar_caractere_especial(senha): # Caractere especial
    caractere_especial = string.punctuation
    return any(c in caractere_especial for c in senha)

def validar_senha(senha):
    erros = []

    verificacoes = [
        (validar_tamanho, "A senha deve ter pelo menos 8 caracteres."),
        (validar_numero, "A senha deve conter pelo menos um número."),
        (validar_minuscula, "A senha deve conter pelo menos uma letra minúscula."),
        (validar_maiuscula, "A senha deve conter pelo menos uma letra maiúscula."),
        (validar_caractere_especial, "A senha deve conter pelo menos um caractere especial (!@#$%^&* etc).")
    ]

    for funcao, mensagem in verificacoes:
        if not funcao(senha): #se validaçao retornar False, adiciona o erro a lista
            erros.append(mensagem)

    return True if not erros else erros # se erro vazio, senha esta correta, se n, retorna os erros

# --- Entrada e Saída de Dados ---
def main():
        loop = True
        while loop is True:

            senha = input("Digite uma senha para validar: ")
            resultado = validar_senha(senha)

            if resultado is True:
                print("✅ Senha forte!")
                loop = False
            else:
                print("❌ Senha fraca. Problemas encontrados:")
                for erro in resultado: #percorre os erros de validar_senha
                    print(f"- {erro}") #formatação organizada
                print("\n🔁 Tente novamente!\n")

if __name__ == "__main__":
    main()  # Chama a função principal