from assistant import Assistant
from speech_recognition_helper import SpeechRecognizer

class Siri:
    def __init__(self):
        self.speech_recognizer = SpeechRecognizer()
        self.assistant = Assistant()

    def start(self):
        self.assistant.speak("Hello dear, How can I help you")
        while True:
            command = self.speech_recognizer.listen()
            self.handle_command(command)

    def handle_command(self, command):
        if 'command mode' in command:
            self.assistant.speak('Command mode activated successfully')
        elif 'play' in command:
            song = command.replace('play', '')
            self.assistant.play_song(song)
        elif 'who is your creator' in command:
            self.assistant.speak("Developer Tarak is my creator")
        elif 'are you single' in command:
            self.assistant.speak("No, I have a boyfriend")
        elif 'who is your boyfriend' in command:
            self.assistant.speak("Tarak, my creator is my boyfriend")
        elif 'good' in command:
            self.assistant.speak('Thank you dear')
        elif 'time' in command:
            self.assistant.get_current_time()
        elif 'tell me about' in command:
            search_pro = command.replace('tell me', '')
            self.assistant.get_wikipedia_info(search_pro)
        elif 'joke' in command:
            self.assistant.tell_joke()
        elif 'thank you' in command:
            self.assistant.speak('You\'re welcome')
        elif 'exit' in command:
            self.assistant.speak('Goodbye!')
            exit()
        else:
            self.assistant.speak("Please say it again")