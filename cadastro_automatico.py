import pyautogui as pa
import pyperclip
import webbrowser
import pandas as pd
from time import sleep


tabela = pd.read_excel('produtos_ficticios.xlsx')
webbrowser.open('https://cadastro-produtos-devaprender.netlify.app/index.html')
sleep(5)

for dados in tabela.index:
    pa.PAUSE = 0.2

    pa.click(x=673, y=297)
    pyperclip.copy(tabela.loc[dados, "Nome do produto"])
    pa.hotkey('ctrl', 'v')
    pa.press('tab')
    pyperclip.copy(tabela.loc[dados, "Descrição"])
    pa.hotkey('ctrl', 'v')
    pa.press('tab')
    pa.write(str(tabela.loc[dados, "Categoria"]))
    pa.press('tab')
    pa.write(str(tabela.loc[dados, "Código do produto"]))
    pa.press('tab')
    pa.write(str(tabela.loc[dados, "Peso (em kg)"]))
    pa.press('tab')
    pa.write(str(tabela.loc[dados, "Dimensões (L x A x P)"]))
    pa.press('tab')  
    pa.press('enter')
    sleep(2)
    pa.press('tab')
    pa.write(str(tabela.loc[dados, "Preço"]))
    pa.press('tab')
    pa.write(str(tabela.loc[dados, "Quantidade em estoque"]))
    pa.press('tab')
    pa.write(str(tabela.loc[dados, "Data de validade"]))
    pa.press('tab')
    pa.write(str(tabela.loc[dados, "Cor"]))
    pa.press('tab')
    pa.write(str(tabela.loc[dados, "Tamanho"]))
    pa.press('tab')
    pa.write(str(tabela.loc[dados, "Material"]))
    pa.click(x=201, y=926)
    sleep(2)
    pa.press('tab')
    pa.write(str(tabela.loc[dados, "Fabricante"]))
    pa.press('tab')
    pa.write(str(tabela.loc[dados, "País de origem"]))
    pa.press('tab')
    pa.write(str(tabela.loc[dados, "Observações"]))
    pa.press('tab')
    pa.write(str(tabela.loc[dados, "Código de barras"]))
    pa.press('tab')
    pa.write(str(tabela.loc[dados, "Localização no armazém"]))
    pa.press('tab')
    pa.press('enter')
    sleep(2)
    pa.press('enter')
    sleep(2)
    pa.click(x=928, y=648)
    sleep(2)

