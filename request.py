import requests
from requests.structures import CaseInsensitiveDict
import json

# URL base
url = 'https://maryhelpflorianopolis-api.mandeumzap.com.br/v1/contacts'

# Declaração de headers
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer 4169287df7661d9c3cd87721a1975e3f7a89611e"

request = requests.get(url, headers = headers)
conteudo = json.loads(request.content)

#numPaginas = conteudo['lastPage']
numPaginas = 5
nomes = []
for number in range(numPaginas):
    number=number+1
    #print ('https://maryhelpflorianopolis-api.mandeumzap.com.br/v1/contacts?page={}'.format(number))
    request = requests.get('https://maryhelpflorianopolis-api.mandeumzap.com.br/v1/contacts?page={}'.format(number), headers = headers)
    conteudo = json.loads(request.content)
    #print(conteudo)
    #data = conteudo['data']
    for id in conteudo['data']:
        print(id["name"])
        nomes.append(id['name'])
#data = conteudo['data']

for name in nomes:
    print(nomes(name))

#for id in data:
#    print(id['name'])


#for value in conteudo["data"]:
#    if value["hadChat"] == 'true':
#        print(value["name"])

#print(request.content)