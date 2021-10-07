import pyttsx3 #pip install pyttsx3
import datetime

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    date = str(datetime.datetime.now().day)
    speak("the date is ")
    speak(date)
    speak(month)
    speak(year)

date()