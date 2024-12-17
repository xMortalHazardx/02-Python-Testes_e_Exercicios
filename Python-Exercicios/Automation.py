import time
#import tkinter as tk
import json
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#template para TKInter


def abrirJS():
    with open('/home/machine/Documents/Python/Files/credentials.json','r') as arquivo:
        todo = json.load(arquivo)
    return todo 

#root= tk.Tk()
#root.title("Chamado Passivo")

#canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
#canvas1.pack()


while True:
    
    
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless=new")
    options.add_argument('window-size=1200x600')
    driver = webdriver.Chrome(options=options)


    
    url = "https://ca.grupocarbel.com.br/SSM/Account/LogOn?opcao=logoff"

    driver.get(url)
    time.sleep(1)
    buton = driver.find_elements(By.ID,"UserName")

    buton[0].send_keys("cesar.emc")
    buton = driver.find_elements(By.ID,"Key")
    buton[0].send_keys("!Caskthebest14")


    buton = driver.find_elements(By.ID,"btnContinuar")
    buton[0].click()

    time.sleep(1)

    buton = driver.find_elements(By.ID,"opcaoBoxNovoChamado")
    buton[0].click()

    buton = driver.find_elements(By.ID,"abrirSelecaoSolicitante")
    buton[0].click()

    buton = driver.find_elements(By.LINK_TEXT,"k-grid-filter")
    buton[0].click()
    
    time.sleep(2)


    driver.quit()