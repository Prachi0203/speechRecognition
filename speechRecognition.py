#succesfully built
import speech_recognition as sr
from time import ctime
import time
import os #it has an attribute remove so it will prevent our audio from piling up
import random  #to randomly generate a file name
import webbrowser
from gtts import gTTS  #it will record our audio
import playsound #it will play instantly not opening our default player

def lucy_speak(audio_string):
    tts = gTTS(audio_string,lang='en')
    r = random.randint(1,1000000)
    audio_file = 'audio_'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
r = sr.Recognizer()
def record_audio(ask=False):
    
    with sr.Microphone() as source:
        if ask:
            lucy_speak(ask)
        voice_data=''
        lucy_speak("say something: ")
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            return voice_data
        except sr.UnknownValueError:   
            lucy_speak('Sorry,I did not get that')
        except sr.RequestError:
            lucy_speak('Sorry,my speech service is down.')
def respond(voice_data):
    if 'what is your name' in voice_data:
        lucy_speak('My name is Lucy')
    if 'what time is it' in voice_data:
        lucy_speak(ctime())
    if 'search' in voice_data:
        search= record_audio('What you want to search for?')
        url='https://google.com/search?q= '+search
        webbrowser.get().open(url)
        lucy_speak('See what I found for '+search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url= 'https://www.google.com/maps/search/?'+location+'/&amp;'
        webbrowser.get().open(url)
        lucy_speak('Here is your location')
    if 'exit' in voice_data:
        print('exit')
        exit()
time.sleep(1)
lucy_speak('How can I help you?')
while 1:
    voice_data=record_audio()
    respond(voice_data)
