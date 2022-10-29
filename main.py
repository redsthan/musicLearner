import pyttsx3
import eyed3
import time
from os import listdir
from os.path import isfile, join
from pygame import mixer
from win10toast import ToastNotifier

toaster = ToastNotifier()

url = "C:\\Users\\Example\\Downloads\\quizz-jazz\\quizz-jazz\\" #dossier avec les musiques dézippé

fichiers = [f for f in listdir(url) if isfile(join(url, f))]

s = pyttsx3.init()
s.setProperty('rate', 100)
s.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
mixer.init()
mixer.music.set_volume(0.7)


def say(artist, title):
    data = "{}, of {}".format(title, artist)
    s.say(data)
    
    s.runAndWait()
    return


def playLearn(file):
    tag = eyed3.load('{}{}'.format(url, file)).tag
    print(tag.title, tag.artist, sep=", of ")
    for _ in range(3):
        say(tag.artist, tag.title)
        toaster.show_toast("Music Learner","\"{}\", of {}".format(tag.title, tag.artist), duration=10)
    return


for file in fichiers:
    mixer.music.load('{}{}'.format(url, file))
    mixer.music.play()
    playLearn(file)
    mixer.music.stop()
