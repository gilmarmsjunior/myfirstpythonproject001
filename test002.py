import FreeSimpleGUI as sg

# Define o layout da janela
layout = [  [sg.Text("Olá, Mundo! Que fácil, hein?")],
            [sg.Button("OK")] ]

# Cria a janela
janela = sg.Window("Janela com PySimpleGUI", layout)

# Loop de eventos para processar "eventos" e obter os "valores" das entradas
while True:
    evento, valores = janela.read()
    # Se o usuário fechar a janela ou clicar em OK
    if evento == sg.WIN_CLOSED or evento == 'OK':
        break

janela.close()