import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from answer import weather, exchange, stock

#문자를 소리로 출력하는 함수(gtts)
def speak(text):
    print('[인공지능]' + text)
    tts = gTTS(text=text, lang='ko')
    file_name = 'data/voice.mp3'
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)
#음성을 듣고 문자로 변환
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        answer(text)
    except sr.UnknownValueError:
        print('인식 실패')
    except sr.RequestError:
        print('요청 실패')


#문자를 입력받아서 대답 인공지능이 대답
def answer(text):
    answer_text = ''
    if '종료' in text:
        answer_text = '다음에 또 만나요'
        speak(answer_text)
        stop(wait_for_stop=False)
        os.exit(0)
    elif '주식' in text:
        index = text.find('주식')
        query = text[:index +2]
        price = stock(query)
        answer_text = f'{text}의 가격은 {price}원 입니다'
    elif '환율' in text:
        rate = exchange()
        answer_text='1달러 환율은' + rate + '원 입니다'
    elif '날씨' in text:
        answer_text= weather()
    elif '안녕' in text:
        answer_text='안녕? 반가워'
    else:
        answer_text='다시 한번 말해줘'
    speak(answer_text)

speak('무엇을 도와드릴까요?')
mic = sr.Microphone()
stop=sr.Recognizer().listen_in_background(mic, listen)

while True:
    pass