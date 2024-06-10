import time
import typing
from PyQt5.QtWidgets import QWidget
import pyttsx3 # text to speech convertable library #
import speech_recognition as sr
import datetime
import sys
import os
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QObject, QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from SNIST_BOT_UI import Ui_SNIST_BOT_UI

# initializtion of text to speech
t2s = pyttsx3.init()

#properties of speech to text#

rate =t2s.getProperty('rate')
'''print(rate)'''
# modify the properties of rate in text to speech #

t2s.setProperty('rate',225)


# modify the voices of text to speech #
#voices = t2s.getProperty('voices')
#t2s.setProperty('voices',voices[1].id)

# to convert text to speech
def speak(audio):
    t2s.say(audio)
    print(audio)
    t2s.runAndWait()

# wishing of users

def Wish():
    hour=int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<=12:
         speak(f"Good morning,its {tt} ")
    elif hour>12 and hour<18:
         speak(f"Good aftenoon,its {tt} ")
    else:
         speak(f"Good evening,its {tt} ")
   # speak("I am snist bot sir. please tell me how can i help you")


class MainThread(QThread):
     def __init__(self):
          super(MainThread,self).__init__()
     def run(self):
          self.tasks()

     # to convert speech to text

     def take_command(self):
            r=sr.Recognizer()
            speak("I am snist bot sir. please tell me how can i help you")
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

        # all the tasks are assigned here
     
     # all the tasks are defined here
     def tasks(self):
            #take_command()
        Wish()
        speak("this is snist bot")
        while True:
            #if 1:
                self.query=self.take_command().lower()
                if "open notepad" in self.query:
                    speak("opening.....")
                    notepad= "C:\\WINDOWS\\system32\\notepad.exe"
                    os.startfile(notepad)

                if "open brave" in self.query:
                     speak("opening brave .....")
                     brave= "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk"
                     os.startfile(brave)

                elif "close notepad" in self.query:
                    speak("closing notepad....")
                    os.system("taskkill /f /im notepad.exe")   
                    ''' elif "no" or "no thanks"or " nothing " in self.query:
                  speak("Thanks for using me sir,have a great day")
                  sys.exit()'''
                #speak("sir do you have any other work")

startmain = MainThread()

class Main(QMainWindow):
    def __init__(self):
          super().__init__()
          self.ui= Ui_SNIST_BOT_UI()
          self.ui.setupUi(self)
          self.ui.pushButton.clicked.connect(self.startTask)
          self.ui.pushButton_2.clicked.connect(self.close)
    def startTask(self):
         #self.ui.movie=QtGui.QMovie("Black_Template.jpg")
         #self.ui.label.setMovie(self.ui.movie)
         #self.ui.movie.start()
         self.ui.movie=QtGui.QMovie("Iron_Template_1.gif")
         self.ui.label_2.setMovie(self.ui.movie)
         self.ui.movie.start()
         self.ui.movie=QtGui.QMovie("Ntuks.gif")
         self.ui.label_3.setMovie(self.ui.movie)
         self.ui.movie.start()
         self.ui.movie=QtGui.QMovie("loading_1.gif")
         self.ui.label_4.setMovie(self.ui.movie)
         self.ui.movie.start()
         self.ui.movie=QtGui.QMovie("Earth.gif")
         self.ui.label_5.setMovie(self.ui.movie)
         self.ui.movie.start()
         self.ui.movie=QtGui.QMovie("initial.gif")
         self.ui.label_6.setMovie(self.ui.movie)
         self.ui.movie.start()
         self.ui.movie=QtGui.QMovie("Hero_Template.gif")
         self.ui.label_7.setMovie(self.ui.movie)
         self.ui.movie.start()
         #self.ui.movie=QtGui.QMovie("Capture.PNG")
         #self.ui.label_9.setMovie(self.ui.movie)
         #self.ui.movie.start()
         timer=QTimer(self)
         timer.timeout.connect(self.showTime)
         timer.start(1000)
         startmain.start()
    def showTime(self):
         current_time=QTime.currentTime()
         current_date=QDate.currentDate()
         label_time=current_time.toString('hh:mm:ss')
         label_date=current_date.toString(Qt.ISODate)
         self.ui.textBrowser.setText(label_date)
         self.ui.text__brower_2.setText(label_time)

app=QApplication(sys.argv)
snist_bot= Main()
snist_bot.show()
exit(app.exec_())

