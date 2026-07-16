import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime


#Initialize Voice engine
engine = pyttsx3.init()

def speak(Text):
    engine.say(Text)
    engine.runAndWait()

def take_commands():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print ("recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    
    except Exception:
        print("sorry,please say that again..")
        return""

def wish_user():
    hour = datetime.datetime.now().hour
    
    if hour < 12:
        speak("Good Morning\n I am your Virtual Assistant")
    elif hour < 18:
        speak("Good afternoon\n I am your Virtual Assistant")
    else:
        speak("Good evening\n I am your Virtual Assistant")
wish_user()

while True:
    command = take_commands()
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%%M %p")
        speak(f"The time is {time}")
        
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com/")

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(command,2)
        print(info)
        speak(info)
    elif("exit") in command:
             speak ("Goodbye")
             break
