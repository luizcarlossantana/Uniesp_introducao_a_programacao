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
