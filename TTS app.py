import PySimpleGUI as sg
import pyttsx3

speaker = pyttsx3.init()

layout = [
    [sg.Text('Enter your text:'),sg.InputText(key='-INPUT-')],
    [sg.Text('Select a voice:'),sg.Radio('Male', "RADIO1", default=True, key='-MALE-'),
     sg.Radio('Female', "RADIO1", key='-FEMALE-'), ],
       [sg.Button('Speak',key='Speak')]
]

window = sg.Window('TEXT TO SPEECH APP', layout,background_color='pink')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Speak':
    
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        
        text = values['-INPUT-']

        voices = engine.getProperty('voices')

        if values['-MALE-']:
            engine.setProperty('voice', voices[0].id)
        elif values['-FEMALE-']:
            engine.setProperty('voice', voices[1].id)
           
        engine.say(text)

        engine.runAndWait()


window.close()
