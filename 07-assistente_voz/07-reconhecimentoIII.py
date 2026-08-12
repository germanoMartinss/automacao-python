import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
from random import randint

# resultado = randint(1, 4)
# numero = int(input("Digite um numero de 1 a 4: "))

def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(audio)
    playsound(audio)
    os.remove(audio)

cria_audio("dados/welcome.mp3", "Escolha um número de 1 a 10")

recon = sr.Recognizer()
with sr.Microphone() as source:
    print("Diga alguma coisa:\n")
    audio = recon.listen(source)

numero_texto = recon.recognize_google(audio, language="pt-BR")
print(f"Você disse: {numero_texto}")

word_to_digit = {
    "um": 1,
    "dois": 2,
    "tres": 3,
    "três": 3,
    "quatro": 4,
    "cinco": 5,
    "seis": 6,
    "sete": 7,
    "oito": 8,
    "nove": 9,
    "dez": 10
}

numero_texto = numero_texto.lower().strip()
if numero_texto.isdigit():
    numero_digito = int(numero_texto)
else:
    numero_digito = word_to_digit.get(numero_texto)

resultado = randint(1, 10)
print(f"O computador escolheu o numero {resultado}")

if numero_digito == resultado:
    print("Parabens, você acertou!")
    cria_audio("dados/resultado.mp3", "Parabens, você acertou!")
else:
    print("Que pena, você errou!")
    cria_audio("dados/resultado.mp3", "Que pena, você errou!")