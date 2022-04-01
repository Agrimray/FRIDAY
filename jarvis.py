import random
import sys
import time
import requests
from requests import get
import pyttsx3
import pyaudio
import webbrowser
import wikipedia
import os
import datetime
import cv2
import pyjokes
import speech_recognition as sr
engine= pyttsx3.init()
voices=engine.getProperty('voices')
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', voice_id)
#print(voices[1].id)
#engine.setProperty('voices',voices[1].id)
#text to speech
def news():
    head=[]
    main_url="https://newsapi.org/v2/top-headlines?country=us&apiKey=40d469c3f1fa4997aed923e223ec646b"
    mainpage=requests.get(main_url).json()
    articles=mainpage["articles"]
    day=["first","second","third","forth","fifth","sizth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        audio=r.listen(source,timeout=100,phrase_time_limit=100)
    try:
        print("Recong......")
        query =r.recognize_google(audio,language='en-in')
        print(f"user-said  :- {query}")
    except Exception as e:
        speak("Say it again plz...")
        return "none"
    return query
#voice t0 text
def wish():
    hour=int(datetime.datetime.now().hour)
    tt=time.strftime("%I:%M %p")
    if hour >=0 and hour <=12:
        speak(f"Good Morning, its {tt}")
    elif hour>12 and hour<18:
        speak(f"Good afternoon, its {tt}")
    else:
        speak(f"Good evening, its {tt}")
    speak("I am Karishma sir. plz ..tel me how may i help you")





if __name__=="__main__":
    #speak('heloo sir')
    wish()
    while True:
        query=takecommand().lower()
        if 'open notepad' in query:
            npath="C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        elif 'open chrome' in query:
            npath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(npath)
        elif "close notepad" in query:
            os.system("taskkill /im notepad.exe")
        elif 'open command prompt' in query:
            npath = "C:\WINDOWS\system32\cmd.exe"
            os.startfile(npath)
        elif "close command prompt" in query:
            os.system("taskkill /im cmd.exe")
        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(10)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllwindows()
        elif "play song" in query:
            music_dir="F:\python coding\jarvis\Music"
            songs=os.listdir(music_dir)
            rd=random.choice((songs))
            os.startfile(os.path.joiwon(music_dir,rd))
        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            speak(f"your ip adress is {ip}")
        elif "wikipedia" in query:
            speak("searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=4)
            speak("according to wikipedia")
            speak(results)
            print(results)
        elif "open youtube" in query:
            speak("what to search in youtube")
            cm = takecommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={cm}")
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
        elif "open google" in query:
            speak("what to search in google")
            cm=takecommand().lower()
            webbrowser.open(f"www.google.com/search?q={cm}")
        elif "tell me a joke" in query:
            joke=pyjokes.get_joke()
            speak(joke)
        elif "no thanks" in query:
            speak("Thanks for using")
            sys.exit()
        elif "set alarm" in query:
            nn=int(datetime.datetime.now().hour)
            if nn==22:
                music="F:\python coding\jarvis\Music"
                songs=os.listdir(music)
                os.startfile(os.path.join(music,songs[0]))
        elif "you can sleep" in query:
            speak("Thanks for using")
            sys.exit()
        elif "tell me news" in query:
            speak("Please wait sir, fetching ....")
            news()
        speak("sir, do u have any other job")








    #takecommand()
    #speak("this is advanced jarvis")
    #sp