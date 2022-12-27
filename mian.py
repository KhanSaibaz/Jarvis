''''
Install these module into your machine 
pip install pyttsx3
pip install speech_recognition
'''
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init("sapi5")
Voice=engine.getProperty('voices')

engine.setProperty('voice',Voice[0].id)  # setting voice 

def Speaker(Audio):
    engine.say(Audio)
    engine.runAndWait()
   
def Wish():
    hour=int(datetime.datetime.now().hour)

    if hour >=0 and hour<=6:
        engine.say("Good Night Sir")

    elif hour >6 and hour<=12:
        engine.say("Good Morning Sir")

    elif hour>12 and hour<=18:
        engine.say("Good AfterNoon Sir")

    elif hour>18 and hour<=24:
        engine.say("Good Evening Sir")
    Speaker("Hii I am Jarvis How can i help you")


def takeCommand():

    '''
    These function take Audio query from user and converted into text and return in string format
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.phrase_threshold=0.5  # It is used for eg If we take a gap of one sec it will not complete the phase
        r.energy_threshold = 200  # minimum audio energy to consider for recording

        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in") # Multiple recognizer are available we used google recongnizer
        print(f"user said : {query}")

    except Exception as e:
        Speaker("Say that again plz...")
        return "None"
    return query

def sendEmail(To,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('20co33@aiktc.ac.in','MYKHAN@786')
    server.send('20co33@aiktc.ac.in',To,content)
    server.close()

if __name__=='__main__':

    Wish()
    while True:
        
        query=takeCommand().lower()
        if 'wikipedia' in query:
            Speaker("seraching wikipedia")
            query=query.replace('wikipedia'," ")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            Speaker(result)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif 'time' in query:
            Times = datetime.datetime.now().strftime(f"%H Hour %M Minutes %S Second")
            # print(Times)
            Speaker(f"Current Time is {Times}")

        elif "open vs code" or 'open visual studio code' in query:
            paths="C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(paths)

        elif 'send email' in query:

            try:
                Speaker("what Should I send")
                content=takeCommand()

                To="khansaibaz2121@gmail.com"
                sendEmail(To,content)
                Speaker("Email has been send")

            except Exception as e:
                Speaker("Soory Not able to send a email")
 

        elif "thanks" in query:
            Speaker("Thank You Sir")
            break

sendEmail('khansaibaz2121@gmail.com',"hello khan")


