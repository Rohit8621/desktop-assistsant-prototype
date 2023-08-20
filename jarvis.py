import webbrowser
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr # pip install speechRecognition
import datetime
import wikipedia # pip install wikipedia
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')

engine.setProperty('voices', voice[0].id)
# print(voices[0].id)

rand_song = random.randint(1,202)
with open('mail.txt', 'r') as f:
    id = f.readline()
    password = f.readline()
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis sir. Please tell me how may I help you")

def takecommand():
    # it takes micrphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        querry=r.recognize_google(audio,language='en-in')
        print(f"User Said: {querry}\n")
    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return querry

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login(id,password)
    server.sendmail(id, to , content)
    server.close()
 

if __name__=='__main__':
    wishMe()
    while True:
    # if 1:
        querry=takecommand().lower()

        # logic for executing tasks based querry
        if 'wikipedia' in querry:
            speak("Searching Wikipedia....")
            querry= querry.replace("Wikipedia","")
            results = wikipedia.summary(querry,sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in querry:
            webbrowser.open("youtube.com")

        elif 'open google' in querry:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in querry:
            webbrowser.open("stackoverflow.com")

        elif 'open linkedin' in querry:
            webbrowser.open("linkedin.com")

        elif 'play music' in querry:
            music_dir="C:\\Users\\RO_HIT\\Music\\LOFI"
            songs= os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[rand_song]))

        elif  'time'  in querry:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"Sir,The time is {strtime} ")
    
        elif 'open code' in querry:
            codepath="C:\\Users\\RO_HIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email rohit' in querry:
            try:
                speak(" What show i say?")
                content = takecommand()
                to = "recievers email...."
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                # print(e)
                speak('Sorry my friend I am not able to send this email')
        elif 'quit' in querry or 'bye' in querry:
            quit()