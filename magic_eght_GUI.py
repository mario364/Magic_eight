import random
import PySimpleGUI as sg


answers = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png',
           '7.png', '8.png', '9.png', '10.png', '11.png',
           '12.png', '13.png', '14.png', '15.png',
           '16.png', '17.png', '18.png', '19.png' ]

layout = [
    [sg.Image('Emty_ball.png', key='img')],
    [sg.Text('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.Введи свой вопрос', key='text')],
    [sg.InputText(key='input'), sg.Button('Спросить')],
    [sg.Button('Выход')]
]


window = sg.Window("Магический шар", layout)



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Спросить':
        if values['input']:
            window['img'].Update(random.choice(answers))
        if not values['input']:
            window['text'].Update('Вы ничего не спросили')

    if event == 'Выход':
        break




window.close()

