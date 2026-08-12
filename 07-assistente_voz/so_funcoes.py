import subprocess
import time
from datetime import datetime
import os

def verifica_hora():
    hora = datetime.now().strftime("%H:%M")
    frase = f"Agora são {hora}"
    return frase

def desliga_computador():
    subprocess.run(["shutdown", "-h", "+60"])

def cancela_desligamento():
    subprocess.run(["shutdown", "-c"])