

from gtts import gTTS
import os
language = 'en'
text = "Hello , there . Thanks for watching my code. By the way my name is sushil gyawali."
sound = gTTS(text=text, lang=language, slow=False)

sound.save("welcome.mp3")

os.system("welcome.mp3")

