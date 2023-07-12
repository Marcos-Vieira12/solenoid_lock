import pyautogui
import time
import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha
# Abrir o terminal (exemplo para linux mint)
pyautogui.press('win')
time.sleep(1)  # Aguardar o terminal abrir
pyautogui.typewrite('cm')
pyautogui.press('enter')
time.sleep(1)  # Aguardar o terminal abrir
pyautogui.typewrite('sudo minicom') # para entrar no ambiente para enviar os dados via serial para a placa
pyautogui.press('enter')
pyautogui.typewrite('25W@#456') #senha do seu sistema
pyautogui.press('enter')

# Exemplo de uso para gerar senhas com 8 caracteres
for i in range(10000):
    senha_gerada = gerar_senha(8)
    pyautogui.typewrite(senha_gerada)
    pyautogui.press('enter')
    time.sleep(1)  # Aguardar o delay de leitura do sistema

