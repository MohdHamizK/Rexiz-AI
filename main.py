import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

r = sr.Recognizer()
engine = pyttsx3.init() 
newsapi = "Your OpenAI API_KEY"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
        tts = gTTS(text)
        filename = "AI-audio.mp3"
        tts.save(filename)

        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()
        os.remove(filename)

def aiProcess(command):
    client = OpenAI(
    api_key="Your OpenAI API_KEY",
)
    command = client.chat.completions.create(
    model="openai/gpt-4o",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Rexiz skilled in general tasks like Alexa and Gemini. Give responses Accordingly please"},
        {"role": "user", "content": command}
    ],
    max_tokens=500 
)

    return command.choices[0].message.content

def processCommand(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in command:
        webbrowser.open("https://instagram.com")
    elif "open twitter" in command:
        webbrowser.open("https://twitter.com")
    elif "open whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
    elif command.startswith("play"):
        song = command.split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}")

    elif "news" in command.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

    else:
        # Let OpenAI handle the request
        response = aiProcess(command)
        speak(response) 

if __name__ == "__main__":
    speak("Initializing Rexiz AI....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word 'Hey Rexiz'...")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                command = r.recognize_google(audio)
                print("Recognized: ", command)
            with sr.Microphone() as mic:
                if (command == "Hey Rexiz"):
                    speak("Yes Boss, How can i help you?")
                    audio = r.listen(mic, timeout=7, phrase_time_limit=3)
                    command = r.recognize_google(audio) 
                    processCommand(command)
                if "exit" in command.lower() or "stop" in command.lower():
                    speak("Goodbye, Shutting down.")
                    break
                processCommand(command)


        except sr.RequestError as e:
            speak("sorry i could not hear you; {0}".format(e))
        except sr.UnknownValueError:
            speak("I could not Hear you")
        except Exception as e:
            speak("An error occurred, please try again.")

            


