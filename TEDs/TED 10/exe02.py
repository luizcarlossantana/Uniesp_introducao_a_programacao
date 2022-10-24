
lista = []
while len(lista) < 30:
   nomes = input("Digite um numero: ")
   lista.append(nomes)
leitura = input('Qual número vc quer procurar ? ')
if leitura in lista:
    print(f'{leitura} apareceu {lista.count(leitura)}')
else:
    print('NÃO ACHEI')
print(lista)

