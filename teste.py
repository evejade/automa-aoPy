import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=791, y=494)
pyautogui.write("oioioi@gmail.com")
pyautogui.press("tab")
pyautogui.write("123")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)
 
tabela= pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=953, y=346)
    codigo= tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")


    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs=tabela.loc[linha, "obs"]
    pyautogui.write(str(tabela.loc[linha, "obs"] ))
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
        
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(50000)