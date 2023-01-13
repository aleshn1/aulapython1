#vamor comecar a aula 1
import webbrowser as wb
import pyautogui
import pyperclip
import time


pyautogui.PAUSE=2
wb.open('www.google.com')
time.sleep(3)
pyautogui.click(x=1169,y=136)
time.sleep(4)
pyautogui.click(x=76,y=196)
time.sleep(2)
pyautogui.click(x=868,y=308)
time.sleep(1)
pyperclip.copy('alessandrohn@hotmail.com')
pyautogui.hotkey('ctrl','v')
pyautogui.click(x=863,y=369)
pyperclip.copy('Segue o relatório de faturamento de vendas')
pyautogui.hotkey('ctrl','v')

#proxima etapa

