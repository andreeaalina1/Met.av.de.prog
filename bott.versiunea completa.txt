import pyautogui
import time

def cautare_google_youtube():
    camp_google = pyautogui.locateOnScreen(
        r"C:\Users\PC\Desktop\bot python versiunea finala\screenn.PNG", confidence=0.6
    )
    if camp_google is not None:
        pyautogui.moveTo(pyautogui.center(camp_google), duration=0.8)  
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.write("https://www.youtube.com/watch?v=b7POCFbJPgs", interval=0.05)  
        pyautogui.press('enter')
        time.sleep(5)  
    else:
        pyautogui.alert("❌ Bara Google nu a fost găsită!")
        return

    coordonate_video = (1371, 516)  # pune coordonatele tale aici
    pyautogui.moveTo(coordonate_video, duration=1)  
    pyautogui.click()
    pyautogui.alert(f"✅ Am dat click pe video la coordonatele {coordonate_video}!")

cautare_google_youtube()
