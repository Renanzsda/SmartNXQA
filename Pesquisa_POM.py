
class Pesquisar:
    def __init__(self, webdriver):
        self.titulo_pesquisa = (By.NAME,"q")
        self.submit = (By.NAME,"btnK")
        self.webdriver = webdriver

    def pesquisar_pagina(self,titulo_pesquisa):  
        self.webdriver.find_element(*self.titulo_pesquisa).send_keys(titulo_pesquisa)
        sleep(2)
        self.webdriver.find_element(*self.submit).click()


#-----------------------------------------------------------------------------------------

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep      

webdriver = Firefox()
url = 'https://www.google.com/'
webdriver.get(url)
todo_pesquisa = Pesquisar(webdriver)

todo_pesquisa.pesquisar_pagina(
    titulo_pesquisa='Teste'
)