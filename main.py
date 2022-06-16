import pyttsx3
import pywhatkit
import time
# import selenium.webdriver as webdriver
import speech_recognition as sr
from keyboard import press
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
# Try using raspberry pie and other sensors for better automation.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning boss!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon boss")   

    else:
        speak("Good Evening boss")  

    speak("what should i do ")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        if 'jarvis' in query:
            speak("yes boss")
        print(f"User said: {query}\n")

    except Exception as e:
        return "what boss?"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def wating():
    query = takeCommand().lower()
    while 'jarvis' not in query:
        query = takeCommand().lower()
    query=query.replace("jarvis","")
    return query
# def get_results(search_term):
#     url="https://in.search.yahoo.com/"
#     browser=webdriver.Chrome()
#     browser.get(url)
#     search_box=browser.find_element_by_id("yschsp")
#     search_box.send_keys(search_term)
#     press('enter')
#     browser.close()
#     print()
#     return 

if __name__ == "__main__":
    wishMe()
    while True:
        query = wating()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'sleep' in query:
            break
        # elif 'who is' or 'search' or 'chrome' or 'internet' in query:
        #     query=query.replace("who is","")
        #     query=get_results(query)
        #     speak(query)
        elif 'play' in query:
            query=query.replace("play","")
            pywhatkit.playonyt(query)
        elif 'open youtube' in query:
            webbrowser.open_new_tab("youtube.com")

        elif 'open google' in query:
            webbrowser.open_new_tab("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open_new_tab("stackoverflow.com")   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")    
            speak(f"Boss, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")    
        else:
            speak("han ji")
