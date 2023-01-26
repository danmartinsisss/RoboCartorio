import pyautogui
from time import sleep

# 0 dois cliques no campo protocolo e limpar campo
pyautogui.doubleClick(132,334)
pyautogui.press('del')
# 1 Inserir Matricula
# 1 digitar protocolo, pressionar enter
pyautogui.click(132,334)

with open('coiso.txt', 'r', encoding='utf8') as arquivo:
    for linha in arquivo:
        protocolo = linha.split(',')[0]

pyautogui.write(protocolo)
pyautogui.press('enter')
pyautogui.press('enter')

sleep(1.5)

# 3 Imprir matricula 380,226
pyautogui.click(383,195)
sleep(0.5)

# Selecionar registro e averbacoes 403,269
pyautogui.click(394,245)
sleep(0.5)

# 242,332 Reimprimir tudo
pyautogui.click(247,303)
sleep(0.5)

# Configuracao de impressao 279,579
pyautogui.click(279,554)
sleep(0.5)

# Custas 2018 334,767
pyautogui.click(321,731)
sleep(0.5)

# margens 322,692
pyautogui.click(327,670)
sleep(0.5)

# Retornar padrao 753,606
pyautogui.click(753,587)
sleep(1.5)

#Imprimir 707,737
pyautogui.click(704,705)
sleep(2)

# Imprimir todas as paginas 55,36
pyautogui.click(61,32)
sleep(2)

# fechar tela 1888,0
pyautogui.click(1888,0)
sleep(2)

# abrir o visual studio
pyautogui.click(1098,1050)

# clicar na aba coiso.txt
pyautogui.click(1609,187)
sleep(3)

# Selecionar e apagar o texto
pyautogui.doubleClick(1432,250)
sleep(1)
pyautogui.press('backspace')
pyautogui.press('del')
pyautogui.press('backspace')

# Clicar na aba imprime matricula
pyautogui.click(1442, 186)

# Clicar em play
pyautogui.click(1793,187)
sleep(1)