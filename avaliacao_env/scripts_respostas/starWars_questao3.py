import requests
import json

#Retorna todos os personagens
reqPeople = requests.get('https://swapi.dev/api/people/').json()
#Retorna todos os planetas
reqPlanets = requests.get('https://swapi.dev/api/planets/').json()

#Declaracao das listas people e planets
people = []
planets = []

#Adiciona a lista people[] apenas os personagens que aparecem em 4 filmes ou mais 
for i in reqPeople['results']:
    if (len(i['films'])>=4):
        people.append(i)

#Adiciona a lista people[] apenas os personagens que aparecem em 4 filmes ou mais
for i in reqPlanets['results']:
    if (len(i['residents'])>=5):
        planets.append(i)

#Criacao de um dicionario respostas para armazenar as consultas realizadas acima
respostas = {'people': people, "planets": planets}

#Escreve os dados encontrados em arquivos JSON chamado respostas.json e em seguida o fecha
with open('respostas.json', 'w') as f:
    json.dump(respostas, f, indent=1)
f.close()