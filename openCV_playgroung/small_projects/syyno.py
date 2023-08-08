import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty("voice",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <=12:
        speak("Good morning ")
    elif(hour>= 12 and hour<18):
        speak("Good afternoon ")
    else:
        speak("good evening ")

    speak(" i am friday your virtual assistant how may i help you ")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 3
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language="en-in")
        print(f"you said {query}")

    except Exception as e:
        print(e)
        print("could you please repeat that ")
        return "None"
    return query

while(True):
    query = take_command().lower()
    if "hello friday" in query:
        wish_me()
        query1 = take_command().lower()
        if "wikipedia" in query1:
            speak("searching in wikipedia......")
            query1.replace("wikipedia","")
            print(query1)
            result = wikipedia.summary(query1, sentences = 2)
            print("According to wikipedia")
            print(result)
            speak(result)

        elif "open youtube" in query1:
            webbrowser.open("youtube.com")

        elif "the time" in query1:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strtime)

        elif "open vs code" in query1:
            codepath = "D:\\vs code\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "quit" in query1:
            exit()



