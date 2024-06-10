import time
import pyttsx3 # text to speech convertable library #
import speech_recognition as sr
import datetime
import sys
import os
t2s = pyttsx3.init()

#properties of speech to text#

'''rate =t2s.getProperty('rate')
print(rate)'''
# modify the properties of rate in text to speech #

t2s.setProperty('rate',125)


# modify the voices of text to speech #
voices = t2s.getProperty('voices')
t2s.setProperty('voices',voices[1].id)

# to convert text to speech
def speak(audio):
    t2s.say(audio)
    print(audio)
    t2s.runAndWait()

# to convert speech to text
def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
    try:
          print("recognising...")
          query = r.recognize_google(audio,language='en-in')
          print(f"user said: {query}")
    except Exception as e:
            speak("say that again please....")
            return "none"
    return query
def Wish():
    hour=int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<=12:
         speak(f"Good morning,its {tt} ")
    elif hour>12 and hour<18:
         speak(f"Good aftenoon,its {tt} ")
    else:
         speak(f"Good evening,its {tt} ")
    speak("I am snist bot sir. please tell me how can i help you")

if __name__=="__main__":
    #take_command()
    Wish()
    #speak("this is snist bot")
    while True:
    #if 1:
         query=take_command().lower()
         if "open notepad" in query:
            speak("opening.....")
            notepad= "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(notepad)

         elif "close notepad" in query:
            speak("closing notepad....")
            os.system("taskkill /f /im notepad.exe")
         
         elif "no thanks"or "nothing" in query:
              speak("Thanks for using me sir,have a great day")
              sys.exit()
        # speak("sir do you have any other work")
         
        





