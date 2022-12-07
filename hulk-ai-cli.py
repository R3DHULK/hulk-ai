import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime,os
import wikipedia,webbrowser
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(r'''
                    _  _ _   _ _    _  __
                   | || | | | | |  | |/ /
                   | __ | |_| | |__| ' < 
                   |_||_|\___/|____|_|\_\
              https://github.com/R3DHULK/hulk-ai  
    ''')

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk("Hi, this is hulk, Your Personal Voice Assistant, How May I Help You?")

def take_command():
    try:
        with sr.Microphone() as source:
            print('\033[92m****Listening****\033[92m')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hulk' in command:
                command = command.replace('hulk', '')
                print(command)
    except:
        pass
    return command


def run_hulk():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'morning' in command:
        talk("good morning")
    elif 'night' in command:
        talk("good night")
    elif 'evening' in command:
        talk("good evening")  
    elif 'night' in command:
        talk("good night")   
    elif 'who are you' in command:
        talk('I Am hulk, Your Personal Voice Assistant')
    elif 'for me' in command:
        talk("I can play songs, tell time, and help you go with wikipedia")
    elif 'current time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'open google' in command:
        webbrowser.open("googlw.com")
    elif 'open stack overflow' in command:
        webbrowser.open("stackoverflow.com")
    elif 'best github projects' in command:
        webbrowser.open("https://github.com/r3dhulk")
    elif 'shutdown' in command:
        talk('I am shutting down')
        os.system("shutdown")
        return False
    elif 'single' in command:
        talk('Sorry, This is out of my league')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_hulk()