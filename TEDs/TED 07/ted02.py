
'''
    Ler o ano atual e o ano de nascimento de uma pessoa. 
    Escrever uma mensagem que diga se ela poderá ou não
    votar este ano (não é necessário considerar o mês
    em que a pessoa nasceu).

'''

ano_atual = 2022
ano_nascer = int(input('Qual seu ano de nascimento ?'))
r = ano_atual-ano_nascer

if r >= 16:
    print(f'Você tem {r} anos  já pode votar, parabéns !!!')
else:
    print('Deu ruim pra tu Boy ! Só vota a partir de 16 anos.')

