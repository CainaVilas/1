# Python com PysimpleGUI
import PySimpleGUI as sg

# layout
sg.theme('reddit')
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario')],
    [sg.Text('senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?', key='salvar')],
    [sg.Button('entrar')]
]

# Janela
janela = sg.Window('tela de login', layout)

# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'entrar':
        if valores['usuario'] == 'jhonatan' and valores['senha'] == '12345':
            print('Bem-vindo Darth Vader')
