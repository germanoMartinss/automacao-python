import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os

def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(audio)
    playsound(audio)
    os.remove(audio)

cria_audio("dados/welcome.mp3", "Ola, eu vou reconhecer sua voz")

recon = sr.Recognizer()
with sr.Microphone() as source:
    print("Diga alguma coisa:\n")
    audio = recon.listen(source)

frase = recon.recognize_google(audio, language="pt-BR")
cria_audio("dados/mensagem.mp3", frase)    