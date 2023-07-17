import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

class Assistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def play_song(self, song):
        self.speak("Playing " + song)
        pywhatkit.playonyt(song)

    def get_current_time(self):
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        self.speak('Current time is ' + current_time)

    def get_wikipedia_info(self, topic):
        try:
            info = wikipedia.summary(topic, 2)
            print(info)
            self.speak(info)
        except wikipedia.exceptions.PageError:
            print("No information found for", topic)
            self.speak("No information found for " + topic)

    def tell_joke(self):
        joke = pyjokes.get_joke()
        print(joke)
        self.speak(joke)