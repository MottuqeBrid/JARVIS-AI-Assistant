import pyttsx3

engine = pyttsx3.init()
# VOICE
voices = engine.getProperty("voices")  # getting details of current voice
# engine.setProperty(
#     "voice", voices[1].id
# )  # changing index, changes voices. 1 for female

for voice in voices:
    print(voice)
