from gtts import gTTS
from playsound import playsound
file_name = 'data/sample.mp3'
text = 'can i help u?'
tts_en = gTTS(text=text, lang='en')
tts_en.save(file_name)
playsound(file_name)