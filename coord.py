import pyautogui
import keyboard

print("Pune mouse-ul pe video și apasă 'x' pentru a salva coordonatele.")

while not keyboard.is_pressed('x'):  # bucla rulează până apeși X
    print(pyautogui.position(), end="\r")  # afișează poziția curentă a mouse-ului

print("\nCoordonate finale:", pyautogui.position())
