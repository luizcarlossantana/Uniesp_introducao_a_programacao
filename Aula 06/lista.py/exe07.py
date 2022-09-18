# 1 froma de fazer isso 

nome = str(input('qual seu nome ? '))
idade = int(input('qual sua idade ?'))
email = str(input('qual seu email ?'))

print(f'Seus dados foram')
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Email: {email}')

# 2 forma de fazer 

lista = [nome,idade,email]
for dados in lista:
    print(dados)