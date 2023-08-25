import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def commands():
    rObj = sr.Recognizer()
    with sr.Microphone() as source:
        print("I AM LISTENING SIR...")
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
       # query="none"
    return query
if __name__ == "__main__":

    while True:

        query = commands().lower()

        if 'who are you' in query:
            speak("I'm a Assistant for you")
        if 'computer' in query:
            speak('yes I am a computer')