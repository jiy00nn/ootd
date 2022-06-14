from gtts import gTTS
import os

class Speech:
    def __init__(self) -> None:
        self.language = 'en'

    def speech(self, temperature, humidity):
        text = f'Today\'s temperature is {temperature} and humidity is {humidity}.'
        print(text)
        myobj = gTTS(text=text, lang=self.language, slow=False)
        myobj.save("speech.mp3")
        os.system("mpg123 speech.mp3")
        os.remove("speech.mp3")
#
# mytext = 'Welcome to geeksforgeeks!'
# language = 'en'
#
# myobj = gTTS(text=mytext, lang=language, slow=False)
#
# myobj.save("welcome.mp3")
#
# os.system("mpg123 welcome.mp3")