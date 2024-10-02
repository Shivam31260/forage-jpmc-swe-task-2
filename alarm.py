import datetime
import pyttsx3
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def ring(alarm_time):
    alarm_time = alarm_time.strip().lower().replace("zira", "").replace("set an alarm", "").replace(" and ", ":")
    print("Alarm set for:", alarm_time)

    # Convert alarm_time string to datetime object
    alarm_time_obj = datetime.datetime.strptime(alarm_time, "%I:%M %p")

    while True:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print("Current time:", current_time)
        
        # Convert current_time string to datetime object
        current_time_obj = datetime.datetime.strptime(current_time, "%I:%M %p")

        if current_time_obj == alarm_time_obj:
            speak("Alarm ringing, Sir")
            os.startfile("music.mp3")
            break  # Break the loop once alarm rings
        elif current_time_obj >= alarm_time_obj:
            print("Alarm time passed.")
            break  # Break the loop if alarm time has passed
        else:
            # Wait for a second before checking again
            datetime.sleep(1)

# Read alarm time from file
with open("Alarmtext.txt", "r") as file:
    alarm_time = file.read()

# Call ring function with extracted time
ring(alarm_time)
