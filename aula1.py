#Automatizando para enviar e-mail com relatório.

import webbrowser as wb
import pyautogui
import pyperclip
import time


pyautogui.PAUSE=2
wb.open('www.google.com')
time.sleep(3)
pyautogui.click(x=1169,y=136)
time.sleep(5)
pyautogui.click(x=76,y=196)
time.sleep(4)
pyautogui.click(x=868,y=308)
time.sleep(2)
pyautogui.write('alessandrohn@hotmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(1)
pyperclip.copy('Relatório de Vendas')
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
#Dados do relatorios ser enviado.
texto = f"" '''

Prezados, segue os dados sobre o faturamento.

O faturamento de ontem foi de:{faturamento} 
A quantidade de produtos foi de:{quantidade}

Att.ale
'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl','v')
time.sleep(1)
pyautogui.hotkey('ctrl','enter')
