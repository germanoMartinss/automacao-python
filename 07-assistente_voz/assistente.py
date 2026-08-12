import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
from random import randint
import sys
import so_funcoes


def cria_audio(audio, mensagem):
    
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(audio)
    playsound(audio)
    os.remove(audio)

def executa_comandos(acao):
    if "fechar assistente" in acao:
        print("Assistente fechado")
        sys.exit()
    elif "horas" in acao:
        cria_audio("dados/horas.mp3", so_funcoes.verifica_hora())
    elif "desligar" in acao and "computador" in acao:
        so_funcoes.desliga_computador()
        cria_audio("dados/desligamento.mp3", "Desligamento programado para daqui a 60 minutos")
    elif "cancelar" in acao and "desligamento" in acao:
        so_funcoes.cancela_desligamento()
        cria_audio("dados/cancelamento.mp3", "Desligamento cancelado")
       
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