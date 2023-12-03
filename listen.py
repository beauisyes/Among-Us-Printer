import speech_recognition
import pyttsx3
from imageprint import printAmongus

recognizer = speech_recognition.Recognizer()

while True:

    try:

        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized {text}")

            count = text.count("among us")
            if count > 0:
                for i in range(count):
                    printAmongus()
            if "stop" in text:
                exit()
                

    except speech_recognition.UnknownValueError():
        recognizer = speech_recognition.Recognizer()
        continue
