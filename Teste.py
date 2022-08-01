from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://www.google.com/'


navegador = Firefox()

navegador.get(url)

sleep(2)

v1 = navegador.find_element(By.NAME,"q")
v1.send_keys("Teste")
sleep(2)
v2 = navegador.find_element(By.NAME,"btnK")
v2.click()





