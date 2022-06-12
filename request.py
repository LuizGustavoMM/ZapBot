import requests
from requests.structures import CaseInsensitiveDict
import json

# URL base
url = 'https://maryhelpflorianopolis-api.mandeumzap.com.br/v1/messages'

# Declaração de headers
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer 4169287df7661d9c3cd87721a1975e3f7a89611e"

request = requests.get(url, headers = headers)

conteudo = json.loads(request.content)

print(conteudo)

#for value in conteudo["data"]:
#    if value["hadChat"] == 'true':
#        print(value["name"])

#print(request.content)