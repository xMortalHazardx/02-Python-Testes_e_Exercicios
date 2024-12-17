import functools
import PySimpleGUI as sg

label = sg.Text("Digite o usuário: ")
input_box = sg.InputText(tooltip="Usuário para o chamado passivo")
add_button = sg.Button("Enviar")

window = sg.Window('Chamado Passivo',layout=[[[label],[input_box, add_button]]])
window.read()
window.close()