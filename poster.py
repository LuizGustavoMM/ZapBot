import requests

url = 'https://webhook.site/9fcab138-8daf-436a-bf83-91c87c93e8ba'

stringMensagem = ("""NOME COMPLETO: Luiz Gustavo
CPF/CNPJ: 000.000.000-00
DATA DE NASCIMENTO: 11/11/1111
E-MAIL: luiz@gmail.com
TELEFONE CELULAR: 48 99999-9999
CEP: 00000-000
ENDEREÇO COMPLETO: servidao manoel costa silveira
NUMERO: 555"""
)

requests.post(url, data=stringMensagem)