# Speech To Text
import speech_recognition as sr

while True:
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        recognize.adjust_for_ambient_noise(source, duration=0.2)
        print('Speak Any...')
        audio = recognize.listen(source)
        try:
            text = recognize.recognize_google(audio)
            print('You Said : {}.'.format(text))
        except:
            print('Sorry Try Again..')
