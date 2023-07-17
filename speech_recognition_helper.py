import speech_recognition as sr

class SpeechRecognizer:
    def __init__(self):
        self.listener = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Siri!! Listening...")
            audio = self.listener.listen(source)
            try:
                text = self.listener.recognize_google(audio)
                print("You:", text)
                return text.lower()
            except sr.UnknownValueError:
                print("Could not understand your voice")
                return ""
            except sr.RequestError:
                print("Failed to connect to speech recognition service")
                return ""