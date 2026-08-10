#1585, 286 1582, 341 1603, 375
import pyautogui
from time import sleep


with open("files/alunos.txt", "r", encoding="utf-8") as file:
    for line in file:
        nome = line.split(",")[0]
        email = line.split(",")[1].strip()
        print(f"Nome: {nome}, Email: {email}")

        pyautogui.moveTo(1585, 286, duration=1.5)
        sleep(1)
        pyautogui.click()
        sleep(1)
        pyautogui.write(nome, interval=0.25)
        pyautogui.moveTo(1582, 341, duration=1.5)
        sleep(1)
        pyautogui.click()
        sleep(1)
        pyautogui.write(email, interval=0.25)   
        pyautogui.moveTo(1603, 375, duration=1.5)
        sleep(1)
        pyautogui.click()   
        pyautogui.screenshot(f"screenshot_chamada.png")