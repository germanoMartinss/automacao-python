import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice", "brazil")


#1-Utilizando o Input
# frase = input("Digite uma frase a ser falada:\n")
# engine.say(frase)
# engine.runAndWait()

#2-Utilizando Arquivo
arquivo = open("dados/frase.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
engine.say(conteudo)
engine.runAndWait()