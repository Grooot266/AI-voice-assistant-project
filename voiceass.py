from tkinter import *

import pyttsx3 
import webbrowser
import os
import wikipedia
import datetime
import speech_recognition as sr 
import smtplib
import random
import youtube_dl
import pyjokes
import wolframalpha
import subprocess
from random import randint as rand
root=Tk()
root.title("Voice Assistant")
root.geometry("500x500")
he='#1e0262'
root.configure(bg=he)



def andrew():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    
    


    def speak(audio):
        engine.say(audio)
        engine.runAndWait()


    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")

        elif hour>=12 and hour<18:
            speak("Good Afternoon!")   

        else:
            speak("Good Evening!")  

        
        
        
        speak("Hello am Andrew. Please tell me how may I help you")
            
     
    

    def takeCommand():
    
        r = sr.Recognizer()
        with sr.Microphone() as source:
            l2.config(text="Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            l3.config(text="Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            a=query
            l4.config(text="User said:"+a+ "\n")

        except Exception as e:
        
            print("Say that again please...")  
            return "None"
        return query

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()
        return()
        


    if __name__ == "__main__":
        wishMe()
        while True:
        # if 1:
            query = takeCommand().lower()

        
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                
                speak("According to Wikipedia")
                l5.config(text="According to Wikipedia:\n"+results)
                speak(results)
                return()

            elif "how are you" in query or "how are you doing" in query:
                l4.config(text="I'm fine sir, how can i help you ?")
                speak("I'm fine sir, how can i help you ?")
                return()

            elif "who are you" in query:
                l5.config(text="I'm andrew voice assistant made by a group of students from B.C.A.")
                speak("I'm andrew voice assistant made by a group of students from B.C.A.")
                return

            elif "what are you doing" in query:
                l5.config(text="Being around to help,just ask if you need anything")
                speak("Being around to help,just ask if you need anything")
                return

        
            elif 'joke'  in query: 
                jk = pyjokes.get_joke()
                speak(jk) 
                l5.config(text='joke:'+jk)
                return

            elif ' tell me a joke'  in query: 
                jk = pyjokes.get_joke()
                l5.config(text='joke:'+jk)
                speak(jk)
                return 

            elif "write a note" in query: 
                speak("What should i write, sir") 
                note = takeCommand() 
                file = open('andrew.txt', 'w') 
                file.write(note)
                return 
           
          
            elif "show the note" in query: 
                speak("Showing Notes") 
                file = open("andrew.txt", "r")  
                l5.config(text=file.read()) 
                speak(file.read(6)) 
                return

            elif "open camera" in query or "camera" in query or "take a photo" in query or "take a click" in query:
                speak("opening camera")
                subprocess.run('start microsoft.windows.camera:', shell=True)
                return

  
            elif 'open netflix' in query:
        
                webbrowser.open("www.netflix.com")
                return

            elif 'search netflix for' in query:
                search_term = query.split("for")[-1]
                url = f"https://netflix.com/search?q={search_term}"
                webbrowser.get().open(url)
                speak(f'Here is what I found for {search_term} on netflix')
                return

        
            elif 'open facebook' in query:
                webbrowser.open("facebook.com")
                return

        

            elif 'open instagram' in query:
                webbrowser.open("instagram.com")
                return

            elif 'open google' in query:
                webbrowser.open("google.com")
                return

        
            elif 'search for' in query or 'search google for' in query:
                search_term = query.split("for")[-1]
                url = f"https://google.com/search?q={search_term}"
                webbrowser.get().open(url)
                speak(f'Here is what I found for {search_term} on google')
                return

            elif 'search google' in query:
                search_term = query.split("google")[-1]
                url = f"https://google.com/search?q={search_term}"
                webbrowser.get().open(url)
                speak(f'Here is what I found for {search_term} on google')
                return

        
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
                return()

            elif 'search youtube for' in query  :
                search_term = query.split("for")[-1]
                url = f"https://youtube.com/search?q={search_term}"
                webbrowser.get().open(url)
                speak(f'Here is what I found for {search_term} on youtube')
                return

            elif 'search in youtube' in query  :
                search_term = query.split("youtube")[-1]
                url = f"https://youtube.com/search?q={search_term}"
                webbrowser.get().open(url)
                speak(f'Here is what I found for {search_term} on youtube')
                return

            elif 'search youtube ' in query  :
                search_term = query.split("youtube")[-1]
                url = f"https://youtube.com/search?q={search_term}"
                webbrowser.get().open(url)
                speak(f'Here is what I found for {search_term} on youtube')
                return

            elif 'open flipkart' in query:
                webbrowser.open("flipkart.com")
                return

            elif 'search flipkart for' in query  :
                search_term = query.split("for")[-1]
                url = f"https://flipkart.com/search?q={search_term}"
                webbrowser.get().open(url)
                speak(f'Here is what I found for {search_term} on flipkart')
                return

            elif 'search in flipkart' in query  :
                search_term = query.split("flipkart")[-1]
                url = f"https://flipkart.com/search?q={search_term}"
                webbrowser.get().open(url)
                speak(f'Here is what I found for {search_term} on flipkart')
                return

            elif 'search flipkart ' in query  :
                search_term = query.split("flipkart")[-1]
                url = f"https://flipkart.com/search?q={search_term}"
                webbrowser.get().open(url)
                speak(f'Here is what I found for {search_term} on flipkart')
                return

        
            elif 'play music' in query or 'play songs' in query:
                music_dir = 'D:\\All mp3 SONGS\\e'
                songs = os.listdir(music_dir)
                l5.config(text='music:'+songs)   

            
                random = os.startfile(os.path.join(music_dir, songs[rand(0,37)]))
                return

            elif 'open amazon' in query:
                webbrowser.open("amazon.in")
                return

            elif 'search amazon for' in query  :
                search_term = query.split("for")[-1]
                url = f"https://www.amazon.in/s?k={search_term}"
                webbrowser.get().open(url)
                speak(f'Here is what I found for {search_term} on amazon')
                return

            elif 'search in amazon' in query  :
                search_term = query.split("amazon")[-1]
                url = f"https://www.amazon.in/s?k{search_term}"
                webbrowser.get().open(url)
                speak(f'Here is what I found for {search_term} on amazon')
                return

            elif 'search amazon ' in query  :
                search_term = query.split("amazon")[-1]
                url = f"https://www.amazon.in/s?k={search_term}"
                webbrowser.get().open(url)
                speak(f'Here is what I found for {search_term} on amazon')
                return


        
        
            elif 'the time' in query or ' what is the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S") 
                l5.config(text='Time:'+strTime)   
                speak(f"Sir, the time is {strTime}")
                return

            elif 'email to ankit' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "ankit101@gmail.com"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                    return
                except Exception as e:
                    l5.config(text=''+e)
                    speak("Sorry, I am not able to send this email")  
                    return 

            elif "where is" in query: 
                query = query.replace("where is", "") 
                location = query 
                speak("User has asked to Locate") 
                speak(location) 
                webbrowser.open("https://www.google.com/maps/place/" + location + "")  
                return

            elif "locate" in query: 
                query = query.replace("locate", "") 
                location = query 
                speak("User has asked to Locate") 
                speak(location) 
                webbrowser.open("https://www.google.com/maps/place/" + location + "") 
                return

            elif "location of" in query: 
                query = query.replace("location of", "") 
                location = query 
                speak("User has asked to Locate") 
                speak(location) 
                webbrowser.open("https://www.google.com/maps/place/" + location + "") 
                return  

            elif "find" in query: 
                query = query.replace("find", "") 
                location = query 
                speak("User has asked to find") 
                speak(location) 
                webbrowser.open("https://www.google.com/maps/place/" + location + "") 
                return 

            elif 'open vs code' in query or 'open visual studio code' in query or 'visual studio code' in query:
                speak("opening visual studio code ")
                codePath = "C:\\Users\\anshu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
                return

            elif 'open ms excel' in query or 'open excel' in query or 'excel' in query or 'open microsoft execel' in query:
                speak("opening microsoft excel ")
                codePath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                os.startfile(codePath)
                return

            elif 'open ms word' in query or 'open word' in query or 'word' in query or 'open microsoft word' in query:
                speak("opening microsoft word ")
                codePath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(codePath)
                return

            elif 'open ms powerpoint ' in query or 'open powerpoint' in query or 'powerpoint' in query or 'open microsoft powerpoint' in query:
                speak("opening microsoft powerpoint")
                codePath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                os.startfile(codePath)
                return

            elif 'quit' in query or 'andrew quit' in query:
                  l5.config (text="Thanks for using andrew")
                  speak("Thanks for using andrew")
                  
                  exit()


    exit()
photo = PhotoImage(file = "micro.png")
root.wm_iconbitmap('icvoi.ico') 
photoImage=PhotoImage(file='vb.png')
lab=Label(root,image=photoImage)
b=Button(root,text='speak',command=andrew,image=photo,bg='yellow')
l1=Label(root,text='Andrew- Voice assistant',bg='orange')


l2=Label(root,text='',bg=he)
l3=Label(root,text='',bg=he)
l4=Label(root,text=' ',bg=he)
l5=Label(root,text='',bg=he)
l1.pack()
lab.pack()


b.pack()
l2.pack()
l3.pack()

l4.pack()
l5.pack()
root.mainloop()
