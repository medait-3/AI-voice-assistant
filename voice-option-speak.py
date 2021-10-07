import pyttsx3 #pip install pyttsx3
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[4].id)   #her change num betw 0and 5
newVoiceRate = 155  #speed of speak
engine.setProperty('rate',newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("this is me")