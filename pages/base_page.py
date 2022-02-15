from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime

class BasePage(object):

    # Мы создаем конструктор, в котором передаются тело браузера и ссылка для дальнейшего использования

    def __init__(self, browser, url, timeout=10):
        super(BasePage, self).__init__()
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def take_screenshot(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        namefile = f"screenshot-{now}.png"
        self.browser.get_screenshot_as_file(namefile)
        print(f"Taked screenshot: {namefile}")




