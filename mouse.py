# Este script captura e exibe a posição atual do cursor do mouse após um atraso de 3 segundos. 
# Útil para identificar coordenadas precisas na tela ao automatizar tarefas com PyAutoGUI.

import pyautogui
import time

time.sleep(3)
print(pyautogui.position())