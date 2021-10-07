import pyttsx3 #pip install pyttsx3
import datetime

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the time is ")
    speak(Time)


def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    date = str(datetime.datetime.now().day)
    speak("the date is ")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome")
    time()
    date()
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour<= 12:
        speak("good morning")
    elif hour >=12 and hour<18:
         speak("good afternoon")
    elif hour >=18 and hour<24:
         speak("good evening")
    else:
        speak("good night")

    speak("how can i help you")
wishme()