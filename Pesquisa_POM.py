from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchText(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # Criar uma sessão no Firefox
        inst.driver = webdriver.Firefox()
        # Navegar até a página do google
        inst.driver.get("http://www.google.com/")
        

    def teste_acessar_comparar_nome_pagina(self):
        # Acessa a pesquisa do google
        self.search_field = self.driver.find_element(By.NAME,"q")
        # Garantir que não vai ter nada e limpa a barra de pesquisa
        self.search_field.clear()
        # Informar o que vai ser pesquisado 
        self.search_field.send_keys("Smart NX")
        # Enviar a requisição e consequentemente realizar a pesquisa
        self.search_field.submit()
        #Adicionar um sleep para dar tempo de carregar a página de pesquisa
        sleep(2)
        #Vai pegar o XPATH para acessar a página solicitada.
        #Foi colocad o h3, pois na pesquisa do google, mostra 3 links iguais, causando conflito
        #Colocando o h3 que é filho de um href único, ou seja apenas um único href tem o h3
        #Captura o elemento
        self.pesquisa = self.driver.find_element(By.XPATH,'//a[@href="https://www.smartnx.com/"]/h3')
        #Clica para acessar o site
        self.pesquisa.click()
        #Adicionar sleep para poder esperar carregar o site
        sleep(2)
        #Vai pegar o elemento do nome e transformar em bolean
        #Se o título da página for igual ao "contains" vai ser true
        self.nome_titulo = self.driver.title.__contains__("Home - Smart NX")
        #Aqui vai ser realizado um assert que espera que seja true a função de cima
        self.assertEqual(True, self.nome_titulo)
        #Aqui vai ser criado uma junção de string, ele vai pegar o text dos elementos e juntar em uma varíavel
        #Vai ser incrimentado na variável do rodape todos os text
        self.rodape =  self.driver.find_element(By.XPATH,'//a[@href="tel:3232122119"]').text
        self.rodape = (self.driver.find_element(By.XPATH,'//a[@href="tel:1131818883"]').text + "\n" + self.rodape )
        self.rodape = (self.driver.find_element(By.XPATH,'//a[@href="tel:5131810491"]').text + "\n" + self.rodape )
        #Para pegar o e-mail foi necessário fazer diferente, como é um link oculto e se fosse fazer parecido com os de cima
        #Iria imprimir o texto igual está no site que seria "e-mail de contado" igual está na (linha 48)
        #Graças ao "get atributes" ele retorna o texto oculto
        self.rodape = (self.driver.find_element(By.XPATH,'//a[@href="mailto:ic@smartnx.io"]').get_attribute("href") + "\n" + self.rodape )
        self.rodape = (self.driver.find_element(By.XPATH,'//a[@href="mailto:ic@smartnx.io"]').text + "\n" + self.rodape )
        print(self.rodape)

        

    #Um metodo que vai fechar o navegador assim que finalizar
    @classmethod
    def tearDownClass(inst):
        #close the browser window
        inst.driver.quit()
#Aqui é uma condicional que vai instanciar o programa
if __name__ == '__main__':
    unittest.main()