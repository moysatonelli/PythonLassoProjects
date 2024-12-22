#João está desenvolvendo um sistema de cadastro para um site de leitura.
#Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. As regras são as seguintes:

#O nome de usuário deve ter pelo menos 5 caracteres.
#A senha deve ter pelo menos 8 caracteres.
#João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas.
#Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

#Crie um programa que implemente essa lógica usando um laço while.

while True:
    username = input("Digite o usuário: ")
    password = input("Digite a senha: ")

    if len(username) >= 5 and len(password) >= 8:
        break
    else:
        print("\nDados inválidos")
        if len(username) < 5:
            print("O usuário deve conter pelo menos 5 caracteres")
        if len(password) < 8:
            print("A senha deve conter pelo menos 8 caracteres")
print(f"\nOlá {username}!\nSeu cadastro foi realizado com sucesso!")