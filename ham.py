import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
from python_play.player import play_it
import sys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('7L7VRK-W5GWKV2KL50')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am your digital assistant LARVIS the Lady Jarvis!')
speak('How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak("Sorry sir! I didn't get that! Try typing the command!")
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('What would you like to watch?')
            ask = myCommand()
            videoname = ask.split()
            ivideoname = '+'.join(map(str,videoname))
            speak('okay')
            webbrowser.open('https://www.youtube.com/search?q='+ivideoname)

        elif 'google it' in query:
            speak('What should I google?')
            ask = myCommand()
            question = ask.split()
            iquestion = '+'.join(map(str,question))
            speak('okay')
            webbrowser.open('https://www.google.com/search?q='+iquestion)

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            music_folder = 'E:\\Music\\'
            speak ('what is the name of the song? ')
            music = myCommand()
            global random_music
            random_music = (music_folder + music + '.mp3')
            speak('Okay, here is your music! Enjoy!')
            play_it(random_music)
            

        elif 'pause music' in query:
            speak("pausing the song")
            random_music.pause()

        elif 'resume music' in query:
            speak("resuming the song")
            random_music.resume()

        elif 'stop music' in query:
            speak("as you say")
            random_music.stop()

        
            
            
            

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                question = query.split()
                iquestion = '+'.join(map(str,question))
                webbrowser.open('https://www.google.com/search?q='+iquestion)
        
        speak('Next Command! Sir!')
        
