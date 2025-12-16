import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
 

# VOICE
voices = engine.getProperty("voices")  # getting details of current voice
engine.setProperty(
    "voice", voices[0].id
)  # changing index, changes voices. 1 for female

engine.setProperty("rate", 170)  # setting up new voice rate


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        print("Yuou said: ...........")
        content=r.recognize_google(audio, language="en-BD"  )
        print("Command: " + content)
    except Exception as e:
        print("Please try again....")
    return content

# speak("Hello, this is a text to speech test.")
