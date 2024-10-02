import pyttsx3
import speech_recognition as sr
import requests
import datetime
from bs4 import BeautifulSoup
import pyautogui
import os
import random
import webbrowser
import math
import importlib  
import pywhatkit
from pygame import mixer
from plyer import notification
from datetime import timedelta
from datetime import datetime
import json
import pyautogui as pt

for i in range(3):
    a = input("Enter password to access Zira: ").strip()  
    with open("password.txt", "r") as pw_file:
        pw = pw_file.read().strip()  

    if a == pw:
        print("WELCOME SIR! PLEASE SPEAK [WAKEUP] TO LOAD ME UP")
        break
    elif i == 2 and a != pw:
        exit()
    elif a != pw:
        print("TRY AGAIN")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def load_data(filepath):
    try:
        with open("conversation_data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return data
def save_data(data, filepath):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    return audio

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Understanding....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said : {query}\n")
        return query.lower()
    except Exception as e:
        print("Say that again please..")
        return "None"

    
# def alarm(query):
#     timehere = open("Alarmtext.txt", "a")
#     timehere.write(query)
#     timehere.close()
#     os.startfile("alarm.py")

def calculate_expression(expression):
    expression = expression.replace('x', '*')
    try:
        # Define additional functions for square, cube, square root, and cube root
        def square(x):
            return x ** 2

        def cube(x):
            return x ** 3

        def sqrt(x):
            return math.sqrt(x)

        def cbrt(x):
            return x ** (1/3)

        # Define operators for basic arithmetic operations
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }
        # Replace words with corresponding symbols
        expression = expression.replace('square', '**2')
        expression = expression.replace('cube', '**3')
        expression = expression.replace('square root', 'sqrt')
        expression = expression.replace('cube root', 'cbrt')

        # Evaluate the mathematical expression
        result = eval(expression, {'__builtins__': None}, {'sqrt': sqrt, 'cbrt': cbrt, **operators})
        return result
    except Exception as e:
        return None
    
# def sendMessage():
#     strTime = int(datetime.now().strftime("%H"))
#     update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))
#     speak("Who do you wan to message")
#     a = int(input('''Person 1 - 1
#     Person 2 - 2'''))
#     if a == 1:
#         speak("Whats the message")
#         message = str(input("Enter the message- "))
#         pywhatkit.sendwhatmsg("+917841887194",message,time_hour=strTime,time_min=update)
#     elif a==2:
#         pass


if __name__ == "__main__":

    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()
            data = load_data("conversation_data.json")
            while True:
                query = takeCommand().lower()
                
                if "rest for sometime" in query:
                    speak(" Ok sir, you can call me anytime ")
                    break

                # elif query in data:
                #     print(data[query])
                #     speak(data[query])
                elif "open personal chatbot" in query:
                    # speak(" Opening Personal Chatbot ")
                    while True:
                        
                        query = takeCommand().lower()
                        # query=input("Question:-")
                        if query in data:
                            print(data[query])
                            speak(data[query])
                        elif"exit the bot" in query:
                            speak(" Ok as you say ")
                            break
                        else:
                            speak("I'm not sure how to respond to that.")
                            response= input(speak("Can you help me with an appropriate response?"))
                            # response=input("Answer:-")
                            data[query] = response
                            save_data(data, "conversation_data.json") 
                            speak("Thanks! I'll remember that for next time.")
                
                elif "what object is this" in query:
                    speak("opening camera to see the object")
                    from Detection import object
                    object()

                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Password changed successfully")
                    speak(f"Your new password is {new_pw}")

                elif"snake game" in query:
                    from Snakegame import game_loop
                    game_loop()
                    break

                elif "schedule my day" in query:
                    tasks = []  # empty list
                    speak("Do you want to clear your old tasks? Please speak yes or no.")
                    query = takeCommand().lower()
                    
                    if "yes" in query:
                        try:
                            # Check if the file exists before truncating
                            if os.path.exists("tasks.txt"):
                                with open("tasks.txt", "w") as file:
                                    file.write(" ")  # Clear the file by writing an empty string
                                print("Old tasks cleared successfully.")
                            else:
                                print("File 'tasks.txt' does not exist.")
                        except Exception as e:
                            print(f"Error clearing old tasks: {e}")

                        no_tasks = int(input("Enter the number of tasks: "))
                        with open("tasks.txt", "w") as file:  # Open in write mode to overwrite old tasks
                            for i in range(no_tasks):
                                task = input(f"Enter task {i + 1}: ")
                                tasks.append(task)
                            file.write(f"{i}. {task}\n")
                    elif "no" in query:
                        no_tasks = int(input("Enter the number of tasks: "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task: "))
                            with open("tasks.txt", "a") as file:
                                file.write(f"{i}. {tasks[i]}\n")

                elif "show my schedule" in query:
                    with open("tasks.txt", "r") as file:
                        content = file.read()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title="My schedule",
                        message=content,
                        timeout=15
                    )
    
                elif "open" in query:
                    query=query.replace("open","")
                    query=query.replace("zira","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press(["enter"])

                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1, 2, 3)  # You can choose any number of songs (I have only chosen 3)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open("https://www.youtube.com/watch?v=ymuNkKuToao&list=RDymuNkKuToao&index=1")
                    elif b == 2:
                        webbrowser.open("https://www.youtube.com/watch?v=ymuNkKuToao&list=RDymuNkKuToao&index=2")
                    elif b == 3:
                        webbrowser.open("https://www.youtube.com/watch?v=ymuNkKuToao&list=RDymuNkKuToao&index=3")

                elif "open" in query:
                    webbrowser.open("https://www.google.com")

                elif 'close' in query:
                    pyautogui.hotkey('ctrl', 'w')

                elif "google" in query:
                    search_query = query.replace("google", "").strip()
                    webbrowser.open(f"https://www.google.com/search?q={search_query}")

                elif "youtube" in query:
                    search_query = query.replace("youtube", "").strip()
                    webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")

                elif "wikipedia" in query:
                    search_query = query.replace("wikipedia", "").strip()
                    webbrowser.open(f"https://en.wikipedia.org/wiki/{search_query}")

                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()
                    # Add your news reading functionality here
                    # speak("Sorry, I don't have the news reading functionality implemented yet.")

                elif "calculate" in query:

                    expression = query.replace("calculate", "").strip()
                    result = calculate_expression(expression)
                    if result is not None:
                        speak(f"The result of {expression} is {result}")
                    else:
                        speak("Sorry, I couldn't calculate that.")

                elif "send a message" in query:
                    current_time = datetime.now()
                    hour = current_time.hour
                    minute = current_time.minute+1
                    x= input("You must provide a number to whom you want to send the message:-  ")
                    y=input("What should the message say:-  ")
                    print(minute)
                    pywhatkit.sendwhatmsg(x,y, hour, minute)
                    pt.click()
                    # timeout=30

                elif "temperature" in query:
                    search = "temperature in mumbai"
                    url = f"https://www.google.co.in/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, 'html.parser')
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"The current {search} is {temp}")

                elif "weather" in query:
                    search = "weather in mumbai"
                    url = f"https://www.google.co.in/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, 'html.parser')
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"The current {search} is {temp}")

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    pyautogui.press("volumeup")
                    # Add your volume up functionality here
                    speak("Turning volume up, sir")

                elif "volume down" in query:
                    pyautogui.press("volumedown")
                    # Add your volume down functionality here
                    speak("Turning volume down, sir")

                elif "what time is it" in query:
                    strTime = datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")

                elif "finally sleep" in query:
                    speak("Going to sleep, sir")
                    exit()

                elif "remember that" in query:
                    speak("what do you want me to remember")
                    rememberMessage = takeCommand().lower()
                    # rememberMessage = query.replace("zira", "")
                    speak("You told me to" + rememberMessage)
                    remember = open("Remember.txt", "a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt", "r")
                    speak("You told me to" + remember.read())

                elif "delete last memory" in query:
                    lines = []
                    try:
                        with open("Remember.txt", "r") as remember_file:
                            lines = remember_file.readlines()
                    except FileNotFoundError:
                        speak("No memories to delete.")
                        continue

                    if lines:
                        last_memory = lines[-1]
                        speak("Are you sure you want to delete the last memory, which is " + last_memory)
                        confirmation = takeCommand().lower()
                        if "yes" in confirmation:
                            with open("Remember.txt", "w") as remember_file:
                                remember_file.writelines(lines[:-1])
                            speak("Last memory has been deleted.")
                        elif "no" in confirmation:
                            speak("Deletion cancelled.")
                    else:
                        speak("No memories to delete.")
                
                elif "shutdown the system" in query:
                    speak("are you sure you want to shutdown the system")
                    shutdown = input("Do you wish to shutdown the Laptop?  (Yes/No)")
                    if shutdown == 'Yes':
                        os.system('shutdown /s /t 1')
                    elif shutdown == "no":
                        break
                
                # else:
                #     speak("Sorry I cant do that.")
                      
                            
