vetor = [

10,20,30,
50,60,70,
3,6,7,91

]

n = vetor[0]
x = vetor[0]

for q in vetor:

    if q > n:
        n = q

    if q < x:
        x = q

print(f'o menor valor {x} e seu indice {vetor.index(x)}')
print(f'o maior valor {n} e seu indice {vetor.index(n)} ')