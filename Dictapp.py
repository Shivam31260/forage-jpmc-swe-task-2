import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

dictapp = {
    "commandprompt": "cmd",
    "paint": "mspaint",
    "word": "winword",
    "excel": "excel",
    "chrome": "chrome",
    "vscode": "code",
    "powerpoint": "powerpnt",
    "calculator": "calc",
    "notepad": "notepad"
}

def openappweb(query):
    speak("Launching Sir.....")
    if ".com" in query or ".org" in query or ".co.in" in query:
        query = query.replace("open ", "")
        query = query.replace("zira ", "")
        query = query.replace("launch ", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")
                return  # Exit the function after opening the specified application
        speak("Sorry, I couldn't find the application you requested.")

def closeappweb(query):
    speak("Closing the application, Sir")
    if "tab" in query:
        if "one tab" in query or "1 tab" in query:
            pyautogui.hotkey("ctrl", "w")
            speak("Tab closed")
        elif "2 tab" in query:
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            speak("Tabs closed")
        elif "3 tab" in query:
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            speak("Tabs closed")
        elif "4 tab" in query:
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            speak("Tabs closed")
        elif "5 tab" in query:
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            speak("Tabs closed")
        else:
            speak("Sorry, I couldn't understand the number of tabs to close.")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
                speak(f"{app.capitalize()} closed")
                return  # Exit the function after closing the specified application
        speak("Sorry, I couldn't find the application you requested.")
