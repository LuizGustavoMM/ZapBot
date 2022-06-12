import requests
from requests.structures import CaseInsensitiveDict

# URL base
url = 'https://maryhelpflorianopolis-api.mandeumzap.com.br/v1/bots'

# Declaração de headers
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer 4169287df7661d9c3cd87721a1975e3f7a89611e"

request = requests.get(url, headers = headers)

conteudo = request.content
print(conteudo)
#print(request.content)