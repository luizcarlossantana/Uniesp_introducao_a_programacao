from requests import get 
from json import dumps

API_KEY = '639d50780031bb94a42a33ddf2cee2d2'
dados = []

while True:
    opçao = input('digite uma opção:\n\
              1 - Adicionar uma cidade na api\n\
              2 - Ver as cidades adicionadas \n\
              3 - Delete uma cidade \n\
              0 - Para sair  \n\
              \nDigite a opação: ')
    
    if opçao == "1":

        cidade = str(input('digite o nome da cidade: '))
        latitude = float(input('digite a latitude da cidade: '))
        longitude = float(input('digite a longitude da cidade: '))
        lista_api = [cidade,latitude,longitude]
        dados.append(lista_api)
    
    elif opçao == "2":
        print(dados)
    
    elif opçao == "3":
        
        item = input("Digite o item que será removido:")

        for i in dados:
            for x in i:
        
                if x == item:
                
                    indice_item = dados.index(i)
                    del dados[indice_item]

        print(indice_item)

    elif opçao == "0":
        break
    else:
        print('deu ruim')

for informaçao in dados:    
   
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={informaçao[1]}&lon={informaçao[2]}&appid={API_KEY}'   
    resposta = get(url)
   

    if resposta.status_code == 200:
        print(f'Criando arquivo: {informaçao[0]}.json')
        with open(informaçao[0] + '.json', 'w', encoding='UTF-8') as arquivo:
            dadosjson = dumps({informaçao[0]:resposta.json()}, indent=4) 
            arquivo.write(dadosjson)
    else:
        print(f'Ocorreu um erro ao consultar as informações para: {informaçao}')


        

