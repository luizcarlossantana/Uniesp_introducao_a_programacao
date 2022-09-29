cadastro = []

botao = 1000
while botao != 0:
    print("Digite 1 para cadastrar um novo usuário.")
    print("Digite 2 para imprimir todos os usuários.")
    print("Digite 0 para sair.")
    botao = int(input("Digite a opção desejada: "))
    if botao == 1:
        nome = input ("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        email = input("Digite o e-mail: ")
        dados = [nome, idade, email]
        cadastro.append(dados)
    
    elif botao == 2:
        for p in cadastro:
            print(p)
            
    elif botao == 0:
        print("Obrigado por acessar esse software.")
        
    else:
        print("Digite um número válido.")