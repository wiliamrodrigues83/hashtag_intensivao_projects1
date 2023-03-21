#automatizacao de processos ou sistema

import openpyxl
import numpy
import time
import pyautogui
import pandas as pd
import os


pyautogui.PAUSE=1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.click(x=671, y=283)
pyautogui.press("enter")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=785, y=455)
pyautogui.write("wiliam")
pyautogui.hotkey("tab")
pyautogui.write("123")
pyautogui.click(x=912, y=665)
time.sleep(2)
pyautogui.click(x=463, y=379, button="right")
time.sleep(2)
pyautogui.click(x=563, y=925, button="left")
time.sleep(2)
pyautogui.click(x=1704, y=982, button="left")


tabela = pd.read_csv(r"C:/Users/UK/IT/Python/HASHTAG/intensivao_hashtag/Aula_1/Compras.csv", sep=";")
print(tabela)
total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = total_gasto/quantidade
print(total_gasto)
print(quantidade)
print(preco_medio)

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.click(x=671, y=283)
pyautogui.press("enter")
pyautogui.write("https://www.gmail.com")
pyautogui.press("enter")
pyautogui.click(x=136, y=273)
pyautogui.write("rodrigues.drum@gmail.com")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.write("Relatorio de Vendas")
pyautogui.hotkey("tab")
pyautogui.write(f"""Good Morning, 
Find below the daily sales report.

Any issue, contact IT team.

Wiliam Rodrigues


Total gasto: R$ {total_gasto:.2f}
Quantidade : {quantidade}
Preco medio : R$ {preco_medio:.2f}
""")
pyautogui.click(x=1216, y=991)











