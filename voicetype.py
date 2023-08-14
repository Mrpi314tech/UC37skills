import pyautogui as pr
import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print('speak...')
    audio=r.listen(source)
    saidtxt=r.recognize_google(audio)
pr.write(saidtxt)