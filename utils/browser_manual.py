from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pathlib import Path

ROOT_PATH = Path(__file__).parents[1]
CHROMEDRIVER_NAME = "chromedriver.exe"
CHROMEDRIVER_PATH = ROOT_PATH / 'bin' / CHROMEDRIVER_NAME

# Especificar o caminho do executável do ChromeDriver
chrome_service = Service(executable_path=CHROMEDRIVER_PATH)

# Para configurar opções do ChromeDriver
chrome_options = webdriver.ChromeOptions()

browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
