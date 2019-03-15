import threading
import pyttsx3
def speaker_call(arg):
    speaker=pyttsx3.init()
    speaker.say('{}'.format(arg))
    speaker.runAndWait()


def announce_class():
    speaker_call('Today is your machine Learning Class')
def start_lecture():
    import os
    os.system("vlc hello.mp4") 

def announce_lunch():
    pass
def start_lecture2():
    pass
def announce_end():
    pass
    
announce_class()



def day_2():
    pass
