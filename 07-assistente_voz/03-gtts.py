from gtts import gTTS
from playsound import playsound

tts = gTTS("Ola, tudo bem?", lang="pt-br")
tts.save("dados/ola.mp3")
playsound("dados/ola.mp3")
