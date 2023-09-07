import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.serProperty('rate', 140)
engine.setProperty('voice', voices[0].id)

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
        print("Processing Sir...")
        query=rObj.recognize_google(audio, language='en-in')
        print(f"You Just said : {query}\n")
    except:
        print("Sorry Try Again..")
        speak("please tell me again sir")
        return None
    return query
    
if __name__ == "__main__":

    while True:
        query = commands().lower()
        
        if 'who are you' in query:
            speak("I'm a Assistant for you")
            
        if 'computer' in query:
            speak('yes I am a computer')
            
        if 'bye' in query:
            speak('bye sir, you can call me anytime!)
            break
