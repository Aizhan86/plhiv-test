from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    def is_element_present(self, how, what, timeout=5):
        try:
            # WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def make(self, action, timeout=5):
        try:
            self.browser.execute_script(action)
            # WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
        return True

    def is_element_clickable(self, how, what):
        try:
            # WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def take_screenshot(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        namefile = f"screenshot-{now}.png"
        self.browser.get_screenshot_as_file(namefile)
        print(f"Taked screenshot: {namefile}")




