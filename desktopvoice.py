import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Set speaking rate

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"User said: {command}")
            return command
    except sr.UnknownValueError:
        talk("Sorry, I didn't understand that.")
    except sr.RequestError:
        talk("Sorry, I'm having trouble connecting to the service.")
    return ""

def run_assistant():
    command = listen_command()
    if 'play' in command:
        song = command.replace('play', '').strip()
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The current time is {time}")
    elif 'who is' in command:
        person = command.replace('who is', '').strip()
        talk(f"Searching for {person}")
        pywhatkit.info(person, lines=1)
    else:
        talk("Sorry, I don't understand that command.")

# Run loop
talk("How can I help you?")
while True:
    run_assistant()