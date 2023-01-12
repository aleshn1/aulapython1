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


