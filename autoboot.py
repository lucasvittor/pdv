import pyautogui
import time
import pandas

pyautogui.doubleClick(x=0, y=446)

time.sleep(2)

pyautogui.write("https://pdv-gilt.vercel.app/")
pyautogui.press("Enter")

time.sleep(1)

table = pandas.read_csv("dba.csv")

for linha in table.index:

        pyautogui.click(x=389, y=226)
        cod = str(table.loc[linha, "codigo"])
        pyautogui.write(cod)

        pyautogui.press("tab")
        marca = str(table.loc[linha, "marca"])
        pyautogui.write(marca)

        pyautogui.press("tab")
        tipo = str(table.loc[linha, "tipo"])
        pyautogui.write(tipo)

        pyautogui.press("tab")
        categoria = str(table.loc[linha, "categoria"])
        pyautogui.write(categoria)

        pyautogui.press("tab")
        preco_unitario = str(table.loc[linha, "preco_unitario"])
        pyautogui.write(preco_unitario)

        pyautogui.press("tab")
        custo = str(table.loc[linha, "custo"])
        pyautogui.write(custo)

        pyautogui.press("tab")
        obs = str(table.loc[linha, "obs"])

        if obs !=  "nan":
                pyautogui.write(obs)    
                
        pyautogui.click(x=468, y=452)    