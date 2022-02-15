import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    s = Service('C:/Users/Aizhan.Orynbayeva/PycharmProjects/PLHIV/venv/Scripts/chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    yield browser
    print("\nquit browser..")
    browser.quit()
