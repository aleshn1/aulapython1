#vamor comecar a aula 1
import webbrowser as wb
import pyautogui
import pyperclip
import time

pyautogui.PAUSE=2
wb.open('www.google.com')
time.sleep(2)
pyautogui.hotkey('ctrl','t')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
time.sleep(2)
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('enter')


time.sleep(3)
print(pyautogui.position())
pyautogui.click(x=338, y=270, clicks=2)
time.sleep(2)
#tela do excel
pyautogui.click(x=462, y=394)
time.sleep(2)
#tres pontinhos
pyautogui.click(x=818, y=159)
#fazer dowload
pyautogui.click(x=619, y=557)
time.sleep(3)