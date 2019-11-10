import speech_recognition as sr
from gtts import gTTS  
import os                 #Google Text-to-Speech

# =============================================================================
# make sure to 
# * pip install SpeechRecognition *  and  * pip install gtts *
# before you proceeeeeeeed
# =============================================================================

voice_inp = ""                       #empty string to store the input

while True:
    speech_recog = sr.Recognizer()
    with sr.Microphone() as source:
        
        try:
            audio = speech_recog.listen(source)
            text = speech_recog.recognize_google(audio)
            print(text)
            if(text == 'stop'):     #say stop to break
                break
            voice_inp += str(text)
        
        except:
            print("Talk Something to get started....!")
            
sound = gTTS(text = voice_inp, lang = 'en', slow = False)
sound.save('inp_sound.mp3')

os.system("inp_sound.mp3") 
