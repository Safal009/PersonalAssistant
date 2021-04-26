import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

dict = {"Aditya":"aditya5656@gmail.com","Mohit":"mrrunwal17@gmail.com","Dad":"shreearihant09@gmail.com","safal":"safal_bhandari@moderncoe.edu.in"}
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good evening")

    speak("I am your Jarvis Please tell me how may i help you Boss?")

def takecommand():
    """This function takes microphone input from the user and returns string output"""
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said: ,{query}\n")

    except Exception as e:
        print(e)

        print("please say that again....")
        return "None"
    return query
def sendemail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("safal_bhandari@moderncoe.edu.in","Safal@09")
    server.sendmail("safal_bhandari@moderncoe.edu.in",to,content)
    server.close()


wishMe()
while True:
      query=takecommand().lower()
      #logic for executing tasks
      if "wikipedia" in query:
          speak("Searching on wikipedia...")
          query=query.replace("wikipedia","")
          results =  wikipedia.summary(query,sentences=1)
          speak("According to wikipedia")
          print(results)
          speak(results)

      elif "open youtube" in query:
          webbrowser.open("youtube.com")

      elif "open google" in query:
          webbrowser.open("google.com")


      elif "songs" in query:
          music_dir = "C:\\MusicFiles"
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir,songs[1]))

      elif "what is the time" in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f" Sir This time is {strTime}")


      elif "open games" in query:
          codepath = "C:\\Games\\Assassins Creed Rogue\\ACC.exe"
          os.startfile(codepath)

      elif "send email" in query:
          try:
              speak("What should i say")
              content = takecommand()
              to = "bhandarisafal512@gmail.com"
              sendemail(to,content)
              speak("Email has been sent")
          except Exception as e:
              speak("Sorry Boss I cannot send your email")



