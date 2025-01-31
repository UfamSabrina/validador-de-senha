🔐 Validador de Senhas em Python
Este é um validador de senhas escrito em Python. Ele verifica se uma senha atende aos critérios mínimos de segurança.

📌 Funcionalidades
✔ Verifica se a senha tem pelo menos 8 caracteres
✔ Confere se contém números
✔ Exige a presença de letras maiúsculas e minúsculas
✔ Garante que tenha pelo menos um caractere especial (!@#$%^& etc.)*
✔ Loop para múltiplas tentativas, até que o usuário insira uma senha forte

🔧 Como executar o código?
📝 1. Clone o repositório
git clone https://github.com/UfamSabrina/validador-de-senha.git
cd validador-de-senhas
💻 2. Execute o script
Windows
python validador.py
Linux/macOS
python3 validador.py
🛠 3. Digite uma senha e veja o resultado
Se a senha for fraca, o programa mostrará os erros e pedirá uma nova senha até que seja forte.

📌 Como importar para outro projeto sem rodar automaticamente?
Se você importar validador.py para outro projeto, ele não será executado sozinho. Para usá-lo, chame a função manualmente:


import validador

senha = "MinhaSenha@123"
resultado = validador.validar_senha(senha)

if resultado is True:
    print("✅ Senha válida!")
else:
    print("❌ Senha fraca:", resultado)
Caso queira que o código rode automaticamente ao ser importado, remova esta parte do final do arquivo:


if __name__ == "__main__":
    main()
Isso fará com que main() seja executado sempre que validador.py for importado.


if __name__ == "__main__":
    main()

  
Isso fará com que main() seja executado assim que validador.py for importado.

