n1 = int(input('digite um número '))
n2 = int(input('digite outro número '))
r = input('qual operação vc deseja fazer')
if r == "+":
    s = n1+n2 
    print(s)
elif r == "-":
    s = n1-n2
    print(s)
elif r == "*":
    s = n1*n2
    print(s)
elif r == "/":
    s = n1/n2
    print(s)
elif r == "**":
    s = n1**n2
    print(s)
else:
    print('Deu ruim pra tu, faz de novo')