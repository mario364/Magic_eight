import random
import PySimpleGUI as sg
import time

answers = ['Бесспорно', 'Предрешено', 'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее '
                                                                                                         'всего',
           'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова', 'Спроси позже',
           'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай',
           'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно' ]

layout = [
    [sg.Image('magic_eight_right.png')],
    [sg.Text('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.Введи свой вопрос')],
    [sg.InputText(key='input'), sg.Button('Спросить')],
    [sg.Text('', visible=False, key='text')]
]


window = sg.Window("Магический шар", layout)



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Спросить':
        if values['input']:
            window['text'].Update(random.choice(answers), visible=True)
        time.sleep(2)
        answer = sg.PopupYesNo('Спросить еще?')
        if answer == 'Yes':
            continue
        else:
            break




window.close()

