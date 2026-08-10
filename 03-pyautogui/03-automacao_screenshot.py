import pyautogui
import time

# #3 - Mover o Mouse para minimizar
pyautogui.moveTo(3756, 19, duration=1.5)
time.sleep(1)
pyautogui.click()
time.sleep(1)


# #4 - Realizando o Scroll
pyautogui.screenshot("screenshot.png")
time.sleep(1)
pyautogui.alert("Screenshot tirada com sucesso!")

while True:
    pyautogui.screenshot(f"screenshot_{time.time()}.png")
    time.sleep(1)
    pyautogui.alert("Screenshot tirada com sucesso!")