import sys, os
print("Python being used:", sys.executable)

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibraray
import requests
from openai import OpenAI

recognizer = sr.Recognizer()
newsapi = "ae9cbbf091fb474bbf2c689efa66e2cf"

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")  )

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('volume', 1.0)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def aiProcess(command):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        
    elif c.lower().startswith("play"):
        song = c.lower().split("play ")[1]
        link = musicLibraray.music[song]
        webbrowser.open(link)
        
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles[:5]:  # limit so it doesn't ramble through 20 headlines
                title = article['title']
                print(title)
                speak(title)
                
        else:
            speak("Sorry, I couldn't fetch the news right now.")
            
    else:
        output = aiProcess(c)
        print(output)
        speak(output)

if __name__ == "__main__":
    speak("Wait Initializing Jarvis...")
    while True:
        r = sr.Recognizer()

        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout = 2, phrase_time_limit = 1)
            word = r.recognize_google(audio)
            print(word)
            if word.strip().lower() == "hello":
                speak("Jarvis Activated")
            
            with sr.Microphone() as source:
                audio = r.listen(source)
                command = r.recognize_google(audio)  # Recognize new audio
                processCommand(command)
            
        except Exception as e:
            print("Error; {0}".format(e))