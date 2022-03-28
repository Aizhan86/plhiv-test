import pytest
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from sys import platform

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    if platform == "linux" or platform == "linux2":
        display = Display(visible=0, size=(800, 600))
        display.start()
        # browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # browser = webdriver.Chrome(service=Service('/usr/local/bin/chromedriver'))
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        browser = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)
        yield browser
        print("\nquit browser..")
        browser.quit()
        display.stop()
    else:
        #browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser = webdriver.Chrome(service=Service('C:/Work/tools/chromedriver/chromedriver.exe'))
        browser.maximize_window()
        yield browser
        print("\nquit browser..")
        browser.quit()



