

API_KEY = '639d50780031bb94a42a33ddf2cee2d2'

from requests import get 
from json import dumps

API_KEY = input("Digite sua chave para utilizar a API: ")
arquivo = input("Informe o arquivo com os dados que deve ser consultados: ")


dados = []
with open(arquivo , 'r', encoding='UTF-8') as x:
    for i in x.readlines():
        print(i)
        i = i.replace('\n','').replace(' ','') 
        formato1 = i.split(',') 
        dados.append(formato1) 

for informaçao in dados:    
   
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={informaçao[3]}&lon={informaçao[2]}&appid={API_KEY}'   
    resposta = get(url)
    print(resposta.text)

    if resposta.status_code == 200:
        print(f'Criando arquivo: {informaçao[0]}.json')
        with open(informaçao[0] + '.json', 'w', encoding='UTF-8') as arquivo:
            dadosjson = dumps({informaçao[1]:resposta.json()}, indent=4) 
            arquivo.write(dadosjson)
    else:
        print(f'Ocorreu um erro ao consultar as informações para: {informaçao}')
