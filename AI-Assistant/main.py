import time
import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import pyautogui
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 145)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def commands():
    rObj = sr.Recognizer()
    with sr.Microphone() as source:
        rObj.pause_threshold=0.9
        rObj.adjust_for_ambient_noise(source,duration=0.5)
        print("Speak Any...")
        audio = rObj.listen(source)
    try:
        print("One Sec...")
        query=rObj.recognize_google(audio, language='en-in')
        print(f"You Just said : {query}\n")
    except:
        print("Sorry Try Again..")
        speak("please tell me again sir")
        query= 'None'
    return query

if __name__ == "__main__":
    while True:

        query = commands().lower()

        if 'still wait' in query:
            speak("ok sir, I'm waiting")
            time.sleep(5)
            speak("I'm Ready waitting your command sir")

        if 'sleep' in query:
            speak("Bye sir, you can call me any time sir.")
            print("Bye sir, you can call me any time sir.")
            break

        if 'search' in query:
            speak("Searching Internet...")
            try:
                query = query.replace("the internet", "")
                query = wikipedia.search(query)
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("I don't know sir, sorry maybe I can't recognize your voice sorry try agin sir")
                print("Try Again")

        if 'time' in query:
            time_var = datetime.datetime.now().strftime("%I:%M:%S")
            speak(f"Sir,the Time is {time_var}")

        if 'day' in query:
            day = datetime.datetime.now().strftime("%A")
            speak(f"today is {day} Sir")

        if 'date' in query:
            date = datetime.datetime.now().strftime("%A:%B:%Y")
            speak(f"today date is {date} Sir")

        if 'open firefox' in query:
            speak("opening firefox sir")
            firefox = "C:/Program Files/Mozilla Firefox/firefox.exe %s"
            webbrowser.get(firefox).open_new("https://google.com")

        if 'open browser' in query:
            speak("opening microsoft edge sir")
            edge = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
            webbrowser.get(edge).open_new("https://google.com")

        if 'open youtube' in query:
            speak('opening youtube sir')
            edge = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
            webbrowser.get(edge).open_new("https://youtube.com")

        if 'open start' in query:
            pyautogui.moveTo(0,475, 1)
            pyautogui.moveTo(74,18, 1)
            pyautogui.click()

        if 'open notepad' in query:
            speak("opening notepad for you sir")
            app_path="C:/Program Files/Sublime Text/sublime_text.exe"
            os.startfile(app_path)
            time.sleep(9)
            pyautogui.moveTo(20,34,1)
            pyautogui.click()
            pyautogui.moveTo(35,53,1)
            pyautogui.click()
            
            
