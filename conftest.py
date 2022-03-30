import pytest
import sentry_sdk
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from sys import platform

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")

    sentry_sdk.init(
        "https://974bf7b634a249f2bf3324d1d4e4387b@debug.ico.kz/27",
        traces_sample_rate=1.0,
    )

    if platform == "linux" or platform == "linux2":
        display = Display(visible=0, size=(800, 600))
        display.start()
        # browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        browser = webdriver.Chrome(service=Service('/usr/local/bin/chromedriver'), options=options)
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



