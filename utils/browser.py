from selenium import webdriver
import time
import os


def make_chrome_browser(*options):
    # configura as opções do ChromeDriver, para ir adicionando posteriormente
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            # adiciona as opções recebidas
            chrome_options.add_argument(option)

    if os.environ.get('SELENIUM_HEADLESS') == '1':
        chrome_options.add_argument("--headless")

    browser = webdriver.Chrome(options=chrome_options)
    return browser


if __name__ == '__main__':
    # cria o navegador com as opções passadas, headless é execução silenciosa
    browser = make_chrome_browser('--headless')
    browser.get("https://google.com")
    time.sleep(5)
