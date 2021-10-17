from sys import exec_prefix
import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr  #pip install SpeechRecognition
import webbrowser
import pywhatkit
import os
import yfinance as yf
import pyjokes
 
def transform():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.3
        said = r.listen(source)
        try:
            print("im listning")
            q = r.recognize_google(said, language="en")
            return q
        except sr.UnknownValueError:
            print("sorry idont unders")
            return "iam waiting"
        except sr.RequestError:
            print("sorry service is  down")
            return "iam waiting"
        except :
            return "iam waiting"
transform()

def speaking(message):
    engine =pyttsx3.init()
    engine.say(message)
    engine.runAndWait()
speaking("hello")
