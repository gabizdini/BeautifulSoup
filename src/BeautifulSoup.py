from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.service import Service


options = Options()
options.headless = True  # Rodar o navegador sem interface gráfica


# Inicializando o ChromeDriver corretamente com as opções
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# URL do site
url = 'https://www.realdist.com.br/marca/santa-amalia.html'


# Acessando a página
driver.get(url)


# Espera até que os elementos dos produtos sejam carregados
try:
   WebDriverWait(driver, 30).until(
       EC.presence_of_element_located((By.CLASS_NAME, 'listagem-item'))
   )


   # Coleta os produtos
   produtos = driver.find_elements(By.CLASS_NAME, 'listagem-item')


   # Exibindo as informações dos produtos
   for produto in produtos:
       try:
           # Pegando o título do produto
           titulo = produto.find_element(By.CLASS_NAME, 'info-produto').text


           # Pegando o link da imagem
           imagem = produto.find_element(By.TAG_NAME, 'img').get_attribute('src')


           print(f'Título: {titulo}')
           print(f'Imagem: {imagem}')
           print('-' * 40)


       except Exception as e:
           print(f'Erro ao extrair dados de um produto: {e}')


finally:
   # Fechar o navegador após a coleta de dados
   sleep(5)
   driver.quit()