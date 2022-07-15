import pytest
import sentry_sdk
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Proxy
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")


    sentry_sdk.init(
        "https://974bf7b634a249f2bf3324d1d4e4387b@debug.ico.kz/27",
        traces_sample_rate=1.0,
    )

    # proxy = Proxy({
    #     'proxyType': ProxyType.MANUAL,
    #     'httpProxy': PROXY1,
    #     'ftpProxy': PROXY1,
    #     'sslProxy': PROXY1,
    #     'noProxy': None
    # })

    # (capabilities = DesiredCapabilities.CHROME())
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument('--no-sandbox')
    # options.add_argument('--headless')
    options.add_argument("--disable-extensions")
    # options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--proxy-server=http://%s' % proxy)
    options.add_argument("test-type")
    # capabilities.setCapability("chrome.binary", "<Path to binary>")
    # capabilities = options.to_capabilities()

    # browser = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME, command_executor="http://127.0.0.1:4444/wd/hub")
    # browser = webdriver.Remote(desired_capabilities=capabilities, command_executor="http://172.18.0.1:4444/wd/hub")
    browser = webdriver.Chrome('/home/user/tool/chromedriver', chrome_options=options)

    # pytest --dist=loadscope --tx 5*popen//python=python3.10 -n 5 --reruns 1 --only-rerun JavascriptException --only-rerun ElementClickInterceptedException testing_test.py

    yield browser
    print("\nquit browser..")
    browser.quit()



