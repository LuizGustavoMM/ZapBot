from multiprocessing.connection import wait
import webbrowser
import selenium
import requests
from selenium import webdriver
from time import sleep
from gettext import install
from webdriver_manager.chrome import ChromeDriverManager


#abrindo o google
navegador = webdriver.Chrome(ChromeDriverManager().install())

#abrindo o mandeumzap
navegador.get("https://maryhelpflorianopolis.mandeumzap.com.br/")

#maximizando a aba
navegador.maximize_window()

#logando no mandeumzap
navegador.find_element_by_xpath('//*[@id="username"]').send_keys("Thais")
navegador.find_element_by_xpath('//*[@id="password"]').send_keys("123456")
navegador.find_element_by_xpath('//*[@id="app"]/div[1]/div/form/button').click()
sleep(10)

#clica na ultima conversa
#navegador.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div[1]/div/div[4]/div[1]/div/div/div[1]').click()

# String exemplo
stringMensagem = ("""NOME COMPLETO: joao costa silveira\n
CPF/CNPJ: 000.000.000-00
DATA DE NASCIMENTO: 11/11/1111
COMO FICOU SABENDO DA MARY HELP:
E-MAIL: joao@gmail.com
TELEFONE CELULAR: 48 99999-9999
CEP: 00000-000
ENDEREÇO COMPLETO: servidao manoel costa silveira
NUMERO: 555"""
)

print(stringMensagem)

#abrindo maryhelper e mudando pra aba
navegador.execute_script('window.open("about:blank", "secondtab");')
navegador.switch_to.window('secondtab')
navegador.get("https://app.maryhelp.net/clientes/cadastro")

#logando no maryhelper
navegador.find_element_by_xpath('//*[@id="txtUser"]').send_keys("JOZEFALEIRO")
navegador.find_element_by_xpath('//*[@id="txtPassword"]').send_keys("123456")
navegador.find_element_by_xpath('//*[@id="login-form"]/button').click()
