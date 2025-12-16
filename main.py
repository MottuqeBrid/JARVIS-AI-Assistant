import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit


def speak(audio):
    print("\n🔊 Speaking:", audio)
    engine = pyttsx3.init()
    # VOICE
    voices = engine.getProperty("voices")  # getting details of current voice
    engine.setProperty(
        "voice", voices[1].id
    )  # changing index, changes voices. 1 for female
    engine.setProperty("rate", 170)  # setting up new voice rate
    engine.stop()
    engine.say(audio)
    engine.runAndWait()


def command():
    content = " "
    while content == " ":
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        # recognize speech using Google Speech Recognition
        try:
            content = r.recognize_google(audio, language="en-BD")
            print("Your Command: " + content)
        except Exception as e:
            print("Please try again....")
    return content


def main():
    while True:
        request = command().lower()
        # Logic for executing tasks based on query
        if "hello" in request:
            speak("Welcome back, Sir. How can I help you?")

        elif "how are you" in request:
            speak("I am fine, Sir. What about you?")
        # play music for you
        elif "play music" in request:
            speak("Playing music for you, Sir.")
            song = random.randint(1, 5)
            if song == 1:
                webbrowser.open(
                    "https://www.youtube.com/watch?v=uKM3hEbLEOg&list=RDuKM3hEbLEOg&start_radio=1"
                )
            elif song == 2:
                webbrowser.open(
                    "https://www.youtube.com/watch?v=uKM3hEbLEOg&list=RDuKM3hEbLEOg&start_radio=1"
                )
            elif song == 3:
                webbrowser.open(
                    "https://www.youtube.com/watch?v=uKM3hEbLEOg&list=RDuKM3hEbLEOg&start_radio=1"
                )
            elif song == 4:
                webbrowser.open(
                    "https://www.youtube.com/watch?v=uKM3hEbLEOg&list=RDuKM3hEbLEOg&start_radio=1"
                )
            elif song == 5:
                webbrowser.open(
                    "https://www.youtube.com/watch?v=uKM3hEbLEOg&list=RDuKM3hEbLEOg&start_radio=1"
                )
        # time and date
        elif "time" in request:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(request)
            speak(f"Sir, the time is {strTime}")

        elif "date" in request:
            strDate = datetime.datetime.now().strftime("%d/%m/%Y")
            speak(f"Sir, today's date is {strDate}")
        # to do list management
        elif "show task" in request or "show my task" in request:
            speak("Your tasks are as follows:")
            try:
                with open("todo/todo.txt", "r") as f:
                    tasks = f.readlines()
                    if not tasks:
                        speak("You have no tasks in your to do list.")
                    else:
                        for idx, task in enumerate(tasks, start=1):
                            speak(f"Task {idx}: {task.strip()}")
            except FileNotFoundError:
                speak("You have no tasks in your to do list.")
        elif (
            "new task" in request
            or "add task" in request
            or "to do" in request
            or "task" in request
        ):
            speak("What is the task?")
            task = command()
            if task == "exit" or task == "exit task" or task == "stop task":
                speak("Exiting task addition.")
            # Here you can add code to save the task to a file or database
            if (
                task != ""
                and task != "exit"
                and task != "exit task"
                and task != "stop task"
            ):
                speak(f"Task {task} has been added to your to do list.")
                with open("todo/todo.txt", "a") as f:
                    f.write(task + "\n")

        elif "show work" in request or "show my work" in request:
            with open("todo/todo.txt", "r") as f:
                tasks = f.read()
                notification.notify(
                    title="Todays Work",
                    message=tasks,
                    timeout=10,
                )

        # open websites
        elif "open youtube" in request:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube for you, Sir.")
        elif "open google" in request:
            webbrowser.open("https://www.google.com")
            speak("Opening Google for you, Sir.")
        elif "open facebook" in request:
            webbrowser.open("https://www.facebook.com")
            speak("Opening Facebook for you, Sir.")
        elif "open github" in request:
            webbrowser.open("https://www.github.com")
            speak("Opening GitHub for you, Sir.")
        elif "open stackoverflow" in request:
            webbrowser.open("https://www.stackoverflow.com")
            speak("Opening Stack Overflow for you, Sir.")
        elif "open gmail" in request:
            webbrowser.open("https://www.gmail.com")
            speak("Opening Gmail for you, Sir.")
        elif "open instagram" in request:
            webbrowser.open("https://www.instagram.com")
            speak("Opening Instagram for you, Sir.")
        # oppen applications
        elif "open" in request:
            app = request.replace("open", "").strip()
            if app != "" or app != "open":
                print(app)
                pyautogui.press("super")
                pyautogui.typewrite(app)
                pyautogui.sleep(2)
                pyautogui.press("enter")
                speak(f"Opening {app} for you, Sir.")

        elif "wikipedia" in request:
            request = (
                request.replace("wikipedia", "")
                .replace("search", "")
                .replace("jarvis", "")
                .strip()
            )
            if request == "":
                speak("Please specify a topic to search on Wikipedia.")
                continue
            print("🔎 Wikipedia search:", request)
            try:
                results = wikipedia.summary(request, sentences=2)
                speak("According to Wikipedia")
                speak(results)

            except wikipedia.exceptions.DisambiguationError:
                speak("The topic is ambiguous. Please be more specific.")

            except wikipedia.exceptions.PageError:
                speak("Sorry, I could not find anything on Wikipedia for that topic.")

            except Exception as e:
                speak("Something went wrong while searching Wikipedia.")
                print(e)

        # send whatsapp message
        elif "send whatsapp message" in request:
            speak("Please provide the phone number, including country code.")
            phone_number = input("Enter the phone number: ")
            speak("What is the message?")
            message = command()
            pywhatkit.sendwhatmsg("+8801308133343", "Hi", 13, 30)
            try:
                pywhatkit.sendwhatmsg_instantly(phone_number, message)
                speak("WhatsApp message sent successfully.")
            except Exception as e:
                speak("Failed to send WhatsApp message.")
                print(e)

        # google search
        elif "search google" in request:
            speak("What should I search on Google?")
            search_query = command().lower()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            speak(f"Here are the Google search results for {search_query}, Sir.")

        # exit program
        elif "exit" in request or "stop" in request or "bye" in request:
            speak("Goodbye, Sir. Have a nice day.")
            break


main()


# speak("Hello, this is a text to speech test.")
