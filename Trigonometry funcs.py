import speech_recognition as sr
import os
import sys
import webbrowser


def talk(words):
    print(words)
    os.system("say " + words)


talk("Чем могу помочь?")

def command():
    spobj = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите")
        spobj.pause_threshold = 1
        audio = spobj.listen(source)
    try:
        usr_word = spobj.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + usr_word)
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        usr_word = command()

    return usr_word


def makeSomething(usr_word):
    if 'открой ютуб' in usr_word:
        talk("Уже открываю")
        url = 'https://youtube.com'
        webbrowser.open(url)
    elif 'стоп' in usr_word:
        talk("Остановка")
        sys.exit()
    elif 'имя' in usr_word:
        talk("Меня зовут Сири")


while True:
    makeSomething(command())

