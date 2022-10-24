''' As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, 
    e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia
    o número de maçãs compradas, calcule e escreva o custo total da compra.
'''

maças = int(input('quantas maçãs você comprou ?'))

if maças < 12 :
    r = maças*1.3
    print(f'O total a pagar será R$ {r}')

else:
    print(f'O total a pagar será R$ {maças}')

