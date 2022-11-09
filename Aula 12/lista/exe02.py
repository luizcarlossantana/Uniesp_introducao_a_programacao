
contador = 0
acumuladora = 0
notas = []

for i in range(20):
    notas.append(float(input('digite uma nota: ')))


for nota in notas:
    acumuladora = acumuladora + nota


media = acumuladora/len(notas)

for n in notas:
    if n > media:
        contador += 1

print(f'{contador} foram as notas acima da média')


'''
se fossemos fazer com uma função interna 
seria: sum(notas)


'''