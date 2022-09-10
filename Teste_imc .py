massa = float(input("qual seu peso em quilogramas?"))
altura =  float( input (" qual sua altura?"))
imc= (massa/(altura**2))

if imc < 18.5:
    print("abaixo do peso")
elif 18.5 <=imc<24.9:
    print("peso ideal(parabéns)")
elif 25<=imc<29.9:
    print("peso ideal(parabéns)")
elif 30<=imc<34.9:
    print("peso ideal(parabéns)")
elif 35<=imc<39.9:
    print("peso ideal(parabéns)")
else:
    print("você está na obesidade III Grau")




    
    





