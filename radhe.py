# pip install SpeechRecognition --> speech recognizing package
# pip install pyttsx3 --> Text to speech package
# pip install PyAudio --> Audio package
# pip install pywhatkit --> for Sending whatsapp message at certain time and to play songs
# pip install wikipedia --> Wikipedia
# pip install pyjokes --> To read out jokes

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)
repeat = True


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=5)
            print("radhe is listening...")
            voice = listener.listen(source)
            print('listened')
            try:
                text = listener.recognize_google(voice)
                print('recognized')
                command = text.lower()
                if 'radhe' in command:
                    command = command.replace("radhe ", "")
                    talk(command)
                    print(command)

            except:
                print("sorry, could not recognise")

    except:
        pass

    return command


def run_radhe():
    command = take_command()

    if "play" in command:
        song = command.replace("play ", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)
        # pywhatkit.sendwhatmsg("+919463034962", song +
        #                      " is playing in youtube now", 10, 46)

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M:%S:%p')
        talk("Current time is "+time)
        print(time)

    elif "wiki" in command or "wikipedia" in command:
        search = command.replace(
            "wiki ", "")
        search = command.replace("wikipedia ", "")
        pywhatkit.search(search)
        info = wikipedia.summary(search, 2)
        talk(info)
        print(info)

    elif 'date' in command:
        talk("Sure, can we meet tonight for dinner date?")

    elif "are you single" in command:
        talk("Yes, I am single")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "quit" in command or "stop" in command:
        global repeat
        talk("Bye my love")
        repeat = False

    else:
        talk("Please say the command again.")


while repeat:
    run_radhe()
