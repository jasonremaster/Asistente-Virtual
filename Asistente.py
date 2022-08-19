import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import locale
from datetime import date

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
joke = pyjokes.get_joke(language='es', category='neutral')
engine.setProperty('voice', 'spanish')
locale.setlocale(locale.LC_TIME, 'es_ES')
wikipedia.set_lang("es")

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Escuchando...')
            voice = listener.listen(source)
            commands = listener.recognize_google(voice, language='es-CO')
            commands = commands.lower()
            if 'alexa' in commands:
                commands = commands.replace('alexa', '')
                print(commands)
    except:
        pass
    return commands


def run_alexa():
    commands = take_command()
    print(commands)

    if 'reproduce' in commands:
        song = commands.replace('play', '')
        talk('Ok, voy a reproducir ' + song + 'en youtube')
        pywhatkit.playonyt(song)
    elif 'hora' in commands:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('La hora es' + time)
    elif 'fecha' in commands:
        fecha = datetime.datetime.now().strftime('%A, %B %d, %Y')
        talk('Hoy estamos: ' + fecha)
    elif 'soltera' in commands:
        talk('No, tengo una relación seria con  el procesador')
    elif 'gracioso' in commands:
        talk(joke)

    elif 'quien es' or 'quién es' in commands:
        person = commands.replace('Quien es ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'como estas' or 'cómo estas':
        talk('Estoy bien gracias')

    else:
        talk('No comprendo, repitelo por favor')


while True:
    run_alexa()
