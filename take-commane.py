import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr  #pip install SpeechRecognition

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def commande():
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        print("listing...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("reconi...")
        query=r.recognize_google(audio,'en=US')
        print(query)
    except Exception as e:
        print(e)
        speak("say again please ... ")

        return "Nne"

    return query

commande()