import pyautogui
import time

# pyautogui.write("Olá, tudo bem? Estou aprendendo a automatizar o teclado com Python e PyAutoGUI!")

pyautogui.press("winleft")
time.sleep(1)
pyautogui.write("Calculator", interval=0.10)
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("123456789", interval=0.25)


#Minimizando 
pyautogui.moveTo(3756, 19, duration=1.5)
time.sleep(1)
pyautogui.click()

#Fecha janela
pyautogui.keyDown("alt")
pyautogui.press("f4")
pyautogui.keyUp("alt")

#Tecla de atalho
pyautogui.hotkey("ctrl", "shift", "esc")

