import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
# from gtts import gTTS
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
# def speak(text):
#     tts = gTTS(text)
#     tts.save('audioresp.mp3') 

def order(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open LinkedIn" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song] # Music Names
        webbrowser.open(link)
        
if __name__ == "__main__":
    speak("Initializing Rexiz ....")
    while True:
        r = sr.Recognizer()
        print("Listening ....")
        try:
            with sr.Microphone() as mic:
                print("I'm Here Boss....")
                audio = r.listen(mic, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if (word.lower() == "Rexiz"):
                speak("Yes Boss, How can i help you?")
                # Listen for command
                with sr.Microphone() as mic:
                    print("Listening....")
                    audio = r.listen(mic, timeout=5, phrase_time_limit=5)
                command = r.recognize_google(audio) 
                order(command)

        except sr.RequestError as e:
            speak("sorry i could not hear you; {0}".format(e))
        except sr.UnknownValueError:
            speak("Rexiz could not understand audio Boss")