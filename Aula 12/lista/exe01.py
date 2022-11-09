'''times = []
while len(times) <= 10:
   nomes = input("Digite um time: ")
   times.append(nomes)
leitura = input('Qual time vc quer procurar ? ')
if leitura in times:
    print('ACHEI')
else:
    print('NÃO ACHEI')
print(times)'''

clubes = []

for i in range(10):
    clube = input('digite um time: ')
    clubes.append(clube)


clube_pesquisar = input('digite um novo time')

for c in clube:
    if clube_pesquisar.upper() == str(c).upper():
        print('achei')
    else:
        print('não achei')