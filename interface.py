from optparse import Values
import PySimpleGUI as sg

def escolha():
#layout
    layout=[[sg.Text('Selecione se o cliente é PJ ou PF: ',size=(30, 1), font='Lucida',justification='left')], 
    [sg.Button('Pessoa física', key=('pf'), font=('Times New Roman',12))],
    [sg.Button('Pessoa juridica', key=('pj'), font=('Times New Roman',12))]] 
#Window
    win = sg.Window('MaryHelper Autocadastro', layout)
#ler os valores
    event, values = win.read()
    if event in ('pf'):
        print('pf')
    else:
        print('pj')
                
#fechar janela após escolha 
    win.close()
#acessa o valor escolhido na lista e adciona a uma string

#display string in a popup         
    sg.popup('O cliente será cadastrado nos próximos minutos!')

escolha()
