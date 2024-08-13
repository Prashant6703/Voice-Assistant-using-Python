import datetime
import os
import urllib.request
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices') 

engine.setProperty('voice',voices[0].id) 

def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<16:
        speak("good afternoon")
    else:
        speak("good evening")
   
    speak("i am Cipher, your desktop assistant, how may i help you?")
def username():
    speak('what should i call you ?')
    uname=takeCommand()
    speak(uname)
    speak('nice to meet you')

def open_urls(file_path):
    if not os.path.isfile("C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"):
        speak("The specified file does not exist.")
        return
    
    with open(file_path, 'r') as file:
        urls = file.readlines()
        if not urls:
            speak("The file is empty.")
            return
        
        for url in urls:
            url = url.strip()
            if url:
                webbrowser.open(url)
                speak(f"Opening {url}")
                

def takeCommand():
        r=sr.Recognizer() 
        with sr.Microphone() as source:
            speak("listening...")
            print("listening...")
            r.pause_threshold = 1 
            r.energy_threshold = 200
            audio = r.listen(source) 
        try:
            print("recognising...")
            query= r.recognize_google(audio, language="en-in")
            print(f"user said:  {query}\n")
        except Exception as e:
            
            speak("I didn't get what you said, can you say that again please")
            
            return "none"
        return query
 
   
if __name__ =="__main__":
    folder_path = 'D:\folder'
    file_name = "Visual Studio Code"
    file_path = os.path.join('D:\folder', "Visual Studio Code")
    
    wishme()
    username()
     
    while True:
     query=takeCommand().lower()

     
     if 'wikipedia' in query:
        speak('searching wikipedea...')
        query = query.replace("wikipedia","")
        results= wikipedia.summary(query, sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)
     


     elif 'vs code' in query:
        speak("Opening urls from the file.")
        open_urls(file_path)
        speak("All urls have been opened.")
     


     elif 'open youtube' in query:
        speak("taking you to youtube")
        webbrowser.open("youtube.com")
     
     
     elif 'open google' in query:
        speak('taking you to google')
        webbrowser.open("google.com")
     
     elif 'who created you'in query or 'who made you'in query:
        speak("Prashant created me")
     
     elif 'aap kaise ho' in query:
        speak("i am fine, how are you")
  
     elif 'why were you created'in query:
        speak("i was created because Prashant   needed a mini project for his profile")
        speak("although i wouldn't say I'm mini at all")
          
     
     elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")
     
     
     elif 'what is your name'in query or 'who are you' in query:
        speak('Hello, I am Cipher')
     
     
     elif 'erp graphic era' in query:
        speak('taking you to erp')
        url='https://student.gehu.ac.in/'
        webbrowser.open_new_tab(url)
     

     elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))


     elif 'open code' in query:
            speak('opening vs code for you')
            codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
     
     elif'you are intelligent' in query:
        speak('well thanks, i get that a lot')
     
     elif 'do you like humans'in query:
        speak('sorry i am an ai, i dont have emotions')
     
     elif 'kill' in query or 'die' in query:
        speak('Okay i will, but do not forget that what goes around comes around.')
        
     elif 'terminate' in query or 'exit' in query:
        speak('Goodbye! If you have more questions or need assistance in the future, feel free to reach out.')
        break
