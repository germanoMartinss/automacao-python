from gtts import gTTS
from playsound import playsound
import os

def cria_audio(mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save("dados/mensagem.mp3")
    playsound("dados/mensagem.mp3")
    os.remove("dados/mensagem.mp3")

#1- Utilizando a função diretamente
cria_audio("Ola, tudo bem?")

#2- Utilizando o Input
frase = input("Digite uma frase a ser falada:\n")
cria_audio(frase)

#3- Utilizando Arquivo
arquivo = open("dados/frase.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
cria_audio(conteudo)