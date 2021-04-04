import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            dax_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            dax_speak('Sorry, I did not get that')
        except sr.RequestError:
            dax_speak('Sorry, my speech service is down')
        return voice_data    

def dax_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if  'how are you' in voice_data:
        dax_speak('I am fine! It is a beautiful day!')
    if  'what is your name' in voice_data:
        dax_speak('My name is Dax')
    if  'what time is it' in voice_data:
        dax_speak(ctime())
    if 'search for' in voice_data:
        search = record_audio('what do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        dax_speak('Here is what I found for ' + search)
    if  'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        dax_speak('Here is the location of ' + location)
    if 'goodbye' in voice_data:
        dax_speak('Bye Caio!')
        exit()
    if 'introduce yourself' in voice_data:
        dax_speak('Hi boss, I am Dax! what you need?')
    if 'you are the best robot' in voice_data:
        dax_speak('I am not a robot')
    if 'you are the best girl' in voice_data:
        dax_speak('I am not a girl')
    if 'so what are you' in voice_data:
        dax_speak('I am your virtual assistant you motherfucker')
    if 'are you like Alexa' in voice_data:
        dax_speak('don\'t you dare talk to me about that bitch')


time.sleep(1)
dax_speak('Hi Caio! welcome back, how can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)