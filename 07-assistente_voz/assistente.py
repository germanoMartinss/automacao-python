import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
from random import randint
import sys


def cria_audio(audio, mensagem):
    
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(audio)
    playsound(audio)
    os.remove(audio)

def executa_comandos(acao):
    if "fechar assistente" in acao:
        print("Assistente fechado")
        sys.exit()
       
def monitora_audio():
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Diga alguma coisa:\n")
            audio = recon.listen(source)
            try:
                mensagem = recon.recognize_google(audio, language="pt-BR")
                mensagem = mensagem.lower()
                print("Você disse: ", mensagem)
                executa_comandos(mensagem)
                break
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                pass
        return mensagem

def main():
    cria_audio("dados/welcome.mp3", "Ola, sou Rita. O que deseja?")
    while True:
        monitora_audio()

main()