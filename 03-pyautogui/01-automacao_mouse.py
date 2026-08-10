import pyautogui
import time

#1 - Tamanho da Tela
print(pyautogui.size())

#2 - Posição do Mouse
print(pyautogui.position())

#3 - Aplicação para verificar a posição do mouse em tempo real
"""
Digite o comando python no terminal:
from pyautogui import mouseInfo
mouseInfo()
"""

#4 - Mover o Mouse para minimizar
pyautogui.moveTo(3756, 19, duration=1.5)
time.sleep(1)
pyautogui.click()

#5 - Realizando o Scroll
# Move o mouse até a posição desejada e clica
pyautogui.moveTo(3832, 745, duration=1.5)
pyautogui.click()
time.sleep(1)

# Realiza o scroll de 500 em 500, até totalizar 4000
total = 4000
passo = 500

for _ in range(total // passo):
    pyautogui.scroll(passo)
    time.sleep(0.2)