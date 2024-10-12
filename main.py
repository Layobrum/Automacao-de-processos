import pyautogui
import time
import pandas as pd

# Definindo o local a ser acessado no futuro
sistemaEmpresa = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Definido um tempo entre os comandos da automação
pyautogui.PAUSE = 0.5

# Abrindo o navegador
pyautogui.press("win")
pyautogui.write("opera") # navegador utilizado
pyautogui.press("enter")
pyautogui.write(sistemaEmpresa) # url do site da empresa
pyautogui.press("enter")

#Definindo um tempo para o site carregar
time.sleep(2)

# Interagindo com a interface do site para fazer login
pyautogui.press("tab")
pyautogui.write("emailteste@gmail.com") # email para logar no site
pyautogui.press("tab")
pyautogui.write("senhaTeste123!") # senha para logar no site
pyautogui.press("enter")

# Definindo um tempo para o site carregar
time.sleep(2)

# Lendo e importando a base de dados
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Criando um loop que passará por cada linha (conjunto de campos)
for linha in range(len(tabela)-1):

    # Criando um loop que passará por cada coluna (campo) da linha
    for coluna in tabela.columns:
        dado = tabela.loc[linha, coluna]  # Pegando o dado contido naquela posição
        pyautogui.press("tab")
        pyautogui.write(str(dado)) #  Inserindo o dado daquela posição no site


    pyautogui.press("enter")
    pyautogui.click(x=310, y=296) # adicionando um clique na tela para resetar o loop e o primeiro tab funcionar
    print(f"A {linha + 1}º ja foi!") # adicionando um contador pra ver se tá funcionando