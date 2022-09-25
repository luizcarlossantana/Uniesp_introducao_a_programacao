'''a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome
personalizado.
c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos
convites. Imprima o nome das pessoas que não poderão comparecer.
d. Modifique sua lista, substitua os desistentes por novos convidados.
e. Exiba um novo convite para cada pessoa que continua presente em sua lista.'''




lista = ['Faustao','Angelica','Danilo gentili','Jô','Neymar']

for convite in lista:
    print(f'você está convidado {convite}.')

#neymar e faustão não podem ir a festa 

for convite in lista:
    print(boolean( input(f'você pode ir a festa {convite} ?')))

print(f'Neymar e Faustão não pedem comparecer.')
    

lista2 = ['luciano hulk','Angelica','Danilo gentili','Jô','cristiano ronaldo']
for convite in lista2:
    print(f'você está convidado  {convite}.')
