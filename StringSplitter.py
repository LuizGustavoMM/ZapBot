# String exemplo
import string

stringMensagem = ("""NOME COMPLETO: joao costa silveira
CPF/CNPJ: 000.000.000-00
DATA DE NASCIMENTO: 11/11/1111
COMO FICOU SABENDO DA MARY HELP: Amigo
E-MAIL: joao@gmail.com
TELEFONE CELULAR: 48 99999-9999
CEP: 00000-000
ENDEREÇO COMPLETO: servidao manoel costa silveira
NUMERO: 555"""
)

#print(stringMensagem)
def splitLines(stringMensagem):
    linhas = []
    linha = ''
    for char in stringMensagem:
        if char != '\n':
            linha += char
        else:
            linhas.append(linha)
            linha = ''

    for linha in linhas:
        strLinha = linha
        stringSpl = strLinha.split(":", 1)
        stringSpace = stringSpl[1]
        print(stringSpace[1])
        string = stringSpace[1:]
        print(string)

    return linhas

splitLines(stringMensagem)

