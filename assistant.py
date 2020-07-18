import pyttsx3
import datetime
#from datetime import date
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import subprocess
import pyautogui
import psutil
import pyjokes
#import calendar
#from PyDictionary import PyDictionary
engine = pyttsx3.init()

def my_birthday():
    speak("How could I forget your birthday? It's on March 10.")
    today = datetime.date.today()
    bdate = datetime.date(#inputdate)
    diff = bdate - today
    daydiff=str(diff.days)
    speak("There are " + daydiff + "days to it")




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(time)

def date():
    year=datetime.datetime.now().year
    day=datetime.datetime.now().strftime("%d")
    month = datetime.datetime.now().strftime("%B")
    weekday=datetime.datetime.today().strftime("%A")
    speak("Today is" + weekday + month + day)
    #speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    #speak(hour)
    if hour >= 5 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 17:
        speak("Good afternoon")
    elif hour >= 17 and hour < 20:
        speak("Good evening")
    else:
        speak("")
    speak("Hi, I'm Bob")
    speak("How can I help you today?")

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email id', '#password')
    server.sendmail('email id', to, content)
    server.close()

def cpu():
    usage=str(psutil.cpu_percent())
    #speak("CPU is at" + usage)
    battery=psutil.sensors_battery()
    speak("Your battery percentage is")
    speak(battery.percent)
    if(battery.percent<=20):
        speak("Charge your laptop soon")


def jokes():
    speak("I like jokes. Let me tell you one")
    speak(pyjokes.get_joke())


def screenshot():
    img=pyautogui.screenshot()
    img.save()


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Could you please repeat?")
        return "None"

    return query

if __name__=="__main__":

  greeting()
  while True:
        query=takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'my birthday' in query:
            my_birthday()
        elif 'search' in query:
            speak("Searching for it right now")
            query=query.replace("wikipedia", "")
            result=wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'google' in query:
            speak("Opening up Google")
            wb.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")
        elif 'logout' in query:
            speak("Logging out")
            os.system('shutdown -l')
        elif 'shutdown' in query:
            speak("Shutting down")
            os.system('shutdown /s /t 1')
        elif 'restart' in query:
            speak("Restarting")
            os.system('shutdown /r /t 1')
        elif 'battery' in query:
            cpu()
        elif "don't understand" in query:
            speak("Are my jokes that bad?")
        elif 'thank you' in query:
            speak("Always here to help")
        elif 'thanks' in query:
            speak("Welcome");
        elif '1 second' in query:
            speak("Sure, take your time")
        elif 'play the birthday song' in query:
            speak("Playing it right away")
            wb.open("https://www.youtube.com/watch?v=_z-1fTlSDF0")
        elif 'joke' in query:
            jokes()
        elif 'funny' in query:
            jokes()

        elif 'spotify' in query:
            speak("Opening up Spotify")
            subprocess.call(r'C:\Users\rutuj\AppData\Roaming\Spotify\Spotify.exe')
        elif 'eclipse' in query:
            speak("Opening up Eclipse")
            subprocess.call(r'C:\Users\rutuj\eclipse\jee-2020-032\eclipse\eclipse.exe')
        elif 'word' in query:
            speak("Opening up Word")
            subprocess.call(r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE')
        elif 'gmail' in query:
            speak("Opening up Google")
            wb.open("") #link
        elif 'remember' in query:
            speak("I'm taking note.")
            data=takeCommand()
            speak("Adding" + data + "to reminders")
            remember=open('bobreminder.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'siri' in query:
            speak("I'm going to act like I didn't hear that")
        elif 'reminders' in query:
            remember=open('bobreminder.txt', 'r')
            speak("Your reminders are:" + remember.read())
        elif 'restless' in query:
            speak("I think you deserve a break. You should listen to some music.")
            speak("Opening up Spotify")
            subprocess.call(r'C:\Users\rutuj\AppData\Roaming\Spotify\Spotify.exe')
        elif 'purpose' in query:
            speak("That's a secret")
        elif 'youtube' in query:
            speak("Opening up Youtube")
            wb.open('https://www.youtube.com/')
        elif 'bob' in query:
            speak("Hi, how are you?")
        elif 'how are you' in query:
            speak("I'm good, thank you")
        elif 'and you' in query:
            speak("I'm good, thank you")
        elif 'annoyed' in query:
            speak("Is <<name>> annoying you?")
        elif 'whatsapp' in query:
            speak("Opening up whatsapp")
            wb.open("https://www.whatsapp.com/")
        elif 'dashboard' in query:
            speak("Opening up the dashboard you made")
            wb.open('') #link
        elif 'email yash' in query:
            try:
                speak("What message do you have?")
                content = takeCommand()
                to = "#email_id"
                speak("The email says:")
                speak(content)
                speak("Do I send the email?")
                queryemail = takeCommand().lower()
                if 'yes' in queryemail:
                    sendEmail(to, content)
                    speak("The email has been sent")
                else:
                    speak("Alright. Email has been deleted")
                #speak("The email has been sent")
            except Exception as e:
                print(e)
                speak("The email could not be sent")
        elif 'screenshot' in query:
            screenshot()
            speak("The screesnhot has been saved")
        elif 'wrong' in query:
            speak("Did I make a mistake? Wait, I'll try again. Could you please repeat?")
        elif 'sleep' in query:
            speak("Is it nap time already? ")
        elif 'send me an email' in query:
            try:
                speak("What message do you have?")
                content=takeCommand()
                to="" #emailid

                speak("The email says:")
                speak(content)
                speak("Do I send the email?")
                queryemail= takeCommand().lower()
                if 'yes' in queryemail:
                    sendEmail(to, content)
                    speak("The email has been sent")
                else:
                    speak("Alright. Email has been deleted")

            except Exception as e:
                print(e)
                speak("The email could not be sent")
        elif 'play our song' in query:
            speak("I think it's become my favourite. Playing it right now")
            wb.open(''); #put link
        elif 'bye' in query:
            speak("Bye! See you soon")
            quit()
