from operator import contains
import requests
import json
import sys

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from requests.structures import CaseInsensitiveDict
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

### Variáveis de request globais
urlGetContent = 'https://webhook.site/token/1dd4c5a1-127f-4159-b710-474f50627ea1'
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

escolha = input("Insira PF para cadastrar uma pessoa física ou PJ para uma pessoa jurídica: ").lower()

if escolha == 'pf':

### Selecionar o cliente a ser cadastrado
        content = json.loads((requests.get(urlGetContent+'/requests', headers=headers).content))
        data = (content['data'])
        nome = input("Insira o nome do cliente a ser cadastrado: ").lower()

        numFound = 0
        listaNomes = []
        for pessoa in data:
            filtroUm = json.loads(pessoa["content"])
            filtroDois = filtroUm["data"]["message"]
            if nome in filtroDois["text"].lower():
                dados = (filtroDois["text"])
                nomeCompleto = (dados.partition('\n')[0])
                if ":" in nomeCompleto:
                    listaNomes.append((nomeCompleto.split(":")[1]))
                else:
                    listaNomes.append(nomeCompleto)
                numFound = numFound + 1

        try: # Exception handling caso não ache ninguém
            if numFound > 1: # Case handling caso a busca retorne mais de um nome
                i = 1
                nomeEscolhido = ""
                print("Encontramos múltiplas ocorrências para esse nome, quais delas gostaria de selecionar?\n")
                for nome in listaNomes:
                    print("{0}. {1}".format(i, nome))
                    i = i + 1
                escolhido = input("Digite o número da sua escolha: ")
                escolhido = int(escolhido)-1
                i = 0
                for nome in listaNomes:
                    if i == escolhido:
                        nomeEscolhido = nome
                    i = i + 1
                
            else:
                nomeEscolhido = listaNomes[0]

        except IndexError:
            print("Não encontramos esse usuário no sistema, por favor tente novamente.")
            sys.exit()

        print("Ok! O sistema irá cadastrar {0}".format(nomeEscolhido))
        
        cliente = nomeEscolhido
        content = json.loads((requests.get(urlGetContent+'/requests', headers=headers).content))
        data = content['data']

        for pessoa in data:
            filtroUm = json.loads(pessoa["content"])
            filtroDois = filtroUm["data"]["message"]
            if cliente in filtroDois["text"]:
                dados = (filtroDois["text"])

        # Script de formatação de dados
        linhas = []
        linha = ''
        print(dados)
        for char in dados:
            if char != '\n':
                linha += char
            else:
                linhas.append(linha)
                linha = ''
        for i in range(len(linhas)):
            
            strLinha = linhas[i]
            if ":" in strLinha:
                stringSpl = strLinha.split(":", 1)
                stringSpace = stringSpl[1]
            else:
                stringSpl = strLinha
                stringSpace = stringSpl
            if (stringSpace[0] == ' '):
                string = stringSpace[1:]
            else:
                string = stringSpace
            linhas[i] = string
            print(linhas[i])
        
        # Filtro para datas de aniversário erradas
        if linhas[2].count('/') == 2:
            linhas[2] = (linhas[2][:5])

        i = 0
        print(linhas[1])

        dados = linhas

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        navegador = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

        # Abrindo navegador e Maryhelp
        navegador.get("https://app.maryhelp.net/clientes/cadastro")
        navegador.maximize_window()

        # Logando no Maryhelp
        navegador.find_element_by_xpath('//*[@id="txtUser"]').send_keys("JOZEFALEIRO")
        navegador.find_element_by_xpath('//*[@id="txtPassword"]').send_keys("123456")
        navegador.find_element_by_xpath('//*[@id="login-form"]/button').click()

        # Caso já tenha alguém conectado, confirmar login
        try:
            logado = navegador.find_element_by_xpath("//*[contains(text(), 'ATENÇÃO!')]")
            if logado:
                navegador.find_element_by_xpath('//*[@id="error_modal"]/div/div/div/div[2]/button[1]').click()
        except:
            pass

        navegador.get("https://app.maryhelp.net/clientes/cadastro")
        sleep(2)

        # Selecionando pessoa física
        navegador.find_element_by_xpath('//*[@id="TypePhysics"]').click()
        sleep(3)

        # Inserindo dados nos campos
        navegador.find_element_by_xpath('//*[@id="txtName"]').send_keys(dados[0])
        navegador.find_element_by_xpath('//*[@id="txtCPF"]').send_keys(Keys.HOME, dados[1])
        navegador.find_element_by_xpath('//*[@id="txtBirthDate"]').send_keys(Keys.HOME, dados[2])
        navegador.find_element_by_xpath('//*[@id="txtEmail"]').send_keys(dados[3])
        navegador.find_element_by_xpath('//*[@id="txtNumber"]').send_keys(Keys.HOME, dados[4])
        navegador.find_element_by_xpath('//*[@id="divInfPess-Content"]/div[7]/div[1]/div[2]/div/input').send_keys(dados[6])
        navegador.find_element_by_xpath('//*[@id="divInfPess-Content"]/div[7]/div[1]/div[3]/div/input').send_keys(dados[5])

elif escolha == 'pj':
        content = json.loads((requests.get(urlGetContent+'/requests', headers=headers).content))
        data = (content['data'])
        nome = input("Insira o nome do cliente a ser cadastrado: ").lower()

        numFound = 0
        listaNomes = []
        for pessoa in data:
            filtroUm = json.loads(pessoa["content"])
            filtroDois = filtroUm["data"]["message"]
            if nome in filtroDois["text"].lower():
                dados = (filtroDois["text"])
                nomeCompleto = (dados.partition('\n')[0])
                if ":" in nomeCompleto:
                    listaNomes.append((nomeCompleto.split(":")[1]))
                else:
                    listaNomes.append(nomeCompleto)
                numFound = numFound + 1

        try: # Exception handling caso não ache ninguém
            if numFound > 1: # Case handling caso a busca retorne mais de um nome
                i = 1
                nomeEscolhido = ""
                print("Encontramos múltiplas ocorrências para esse nome, quais delas gostaria de selecionar?\n")
                for nome in listaNomes:
                    print("{0}. {1}".format(i, nome))
                    i = i + 1
                escolhido = input("Digite o número da sua escolha: ")
                escolhido = int(escolhido)-1
                i = 0
                for nome in listaNomes:
                    if i == escolhido:
                        nomeEscolhido = nome
                    i = i + 1
                
            else:
                nomeEscolhido = listaNomes[0]

        except IndexError:
            print("Não encontramos esse usuário no sistema, por favor tente novamente.")
            sys.exit()

        print("Ok! O sistema irá cadastrar {0}".format(nomeEscolhido))
        
        cliente = nomeEscolhido
        content = json.loads((requests.get(urlGetContent+'/requests', headers=headers).content))
        data = content['data']

        for pessoa in data:
            filtroUm = json.loads(pessoa["content"])
            filtroDois = filtroUm["data"]["message"]
            if cliente in filtroDois["text"]:
                dados = (filtroDois["text"])

        # Script de formatação de dados
        linhas = []
        linha = ''
        print(dados)
        for char in dados:
            if char != '\n':
                linha += char
            else:
                linhas.append(linha)
                linha = ''
        for i in range(len(linhas)):
            
            strLinha = linhas[i]
            if ":" in strLinha:
                stringSpl = strLinha.split(":", 1)
                stringSpace = stringSpl[1]
            else:
                stringSpl = strLinha
                stringSpace = stringSpl
            if (stringSpace[0] == ' '):
                string = stringSpace[1:]
            else:
                string = stringSpace
            linhas[i] = string
            print(linhas[i])

        i = 0
        print(linhas[1])

        dados = linhas

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        navegador = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

        # Abrindo navegador e Maryhelp
        navegador.get("https://app.maryhelp.net/clientes/cadastro")
        navegador.maximize_window()

        # Logando no Maryhelp
        navegador.find_element_by_xpath('//*[@id="txtUser"]').send_keys("JOZEFALEIRO")
        navegador.find_element_by_xpath('//*[@id="txtPassword"]').send_keys("123456")
        navegador.find_element_by_xpath('//*[@id="login-form"]/button').click()

        # Caso já tenha alguém conectado, confirmar login
        try:
            logado = navegador.find_element_by_xpath("//*[contains(text(), 'ATENÇÃO!')]")
            if logado:
                navegador.find_element_by_xpath('//*[@id="error_modal"]/div/div/div/div[2]/button[1]').click()
        except:
            pass

        navegador.get("https://app.maryhelp.net/clientes/cadastro")
        sleep(2)

        # Selecionando pessoa física
        navegador.find_element_by_xpath('//*[@id="TypePhysics"]').click()
        sleep(3)

        # Inserindo dados nos campos
        navegador.find_element_by_xpath('//*[@id="txtCorporateName"]"]').send_keys(dados[0])
        navegador.find_element_by_xpath('//*[@id="txtCNPJ"]').send_keys(Keys.HOME, dados[1])
        navegador.find_element_by_xpath('//*[@id="divInfPess-Content"]/div[7]/div[1]/div[3]/div/input').send_keys(Keys.HOME, dados[2])
        navegador.find_element_by_xpath('//*[@id="txtNameRepresentative"]').send_keys(dados[3])
        navegador.find_element_by_xpath('//*[@id="txtCPFRepresentative"]').send_keys(Keys.HOME, dados[4])
        navegador.find_element_by_xpath('//*[@id="txtEmail"]').send_keys(dados[5])
        navegador.find_element_by_xpath('//*[@id="txtNumber"]').send_keys(dados[6])
else:
    print('Escolha incorreta!')
    sleep(10)

