import pyautogui as pr
import speech_recognition as sr
import os
r=sr.Recognizer()
os.system('espeak -ven-us "what do you want to type?')
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    audio=r.listen(source)
    saidtxt=r.recognize_google(audio)
pr.write(saidtxt)