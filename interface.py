import PySimpleGUI as sg

dados = str('dados_cadastrais_dos_clientes_provenientes_do_webhook')

#layout
layout=[[sg.Text('Lista mais recente de clientes: ',size=(30, 1), font='Lucida',justification='left')],
        [sg.Listbox(values=[dados], select_mode='extended', size=(30, 6))],        
        [sg.Button('Cadastrar', font=('Times New Roman',12)),sg.Button('Cancelar', key=('cadatrar'), font=('Times New Roman',12))]]
#Window
win = sg.Window('MaryHelper Autocadastro',layout)
#ler os valores
e,v = win.read()
#fechar janela após escolha
win.close()
#acessa o valor escolhido na lista e adciona a uma string
        
#display string in a popup         
sg.popup('O cliente será cadastrado nos próximos minutos!')
