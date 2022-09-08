massa = float (input ("Diga seu peso em quilograma"))
altura = float (input("Diga a sua altura em metros"))
imc = (massa/(altura**2))

if imc <18.5:
    print ("Seu IMC é de", imc)
    print ("Abaixo do peso ideal, procure um especialista")
elif 18.5< imc <24.99:
    print ("Seu IMC é de", imc)
    print ("Peso Normal")
elif 25< imc <30.00:
    print ("Seu IMC é de", imc)
    print ("Sobrepeso, procure um especialista")
else:
    print ("Seu IMC é de", imc)
    print ("Obesidade, procure um especialista")