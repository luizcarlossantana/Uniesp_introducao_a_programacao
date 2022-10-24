



''' 
Escreva um algoritmo que permita a leitura dos 
nomes de 10 clubes de futebol e armazene os nomes 
lidos em um vetor (lista). Após isto, o algoritmo deve 
permitir a leitura de mais 1 nome qualquer de clube e 
depois escrever a mensagem ACHEI, se o nome estiver entre 
]os 10 nomes lidos anteriormente (guardados no vetor), 
ou NÃO ACHEI caso contrário

'''



times = []
while len(times) <= 10:
   nomes = input("Digite um time: ")
   times.append(nomes)
leitura = input('Qual time vc quer procurar ? ')
if leitura in times:
    print('ACHEI')
else:
    print('NÃO ACHEI')
print(times)






'''
Faça um algoritmo para ler um vetor de 30 
números. Após isto, ler mais um número qualquer, 
calcular e escrever 
quantas vezes esse número aparece no vetor.
'''





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

