from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class Driver:
    '''Provides automatically manage of drivers for different browsers'
    https://pypi.org/project/webdriver-manager/

    Installation:
        pip install webdriver-manager
    https://github.com/SergeyPirogov/webdriver_manager/tree/master
    NB: Opera browser does`t supported

    Desired.Capabilities is going to be implemented soon'
    '''

    def __init__(self, browser):
        self.browser = browser

    def set_browser(self, mode):
        '''mode is set to True, runs tests in silent mode: no UI while testing'''

        if self.browser.lower() == "firefox":
            options = FirefoxOptions()
            options.headless = mode
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

        elif self.browser.lower() == "chrome":
            options = Options()
            options.headless = mode
            # options.add_argument('--disable-gpu')
            # options.add_argument("--no-sandbox")
            # options.add_argument("window-size=1400,2100")  # Linux should be activate
            return webdriver.Chrome(ChromeDriverManager().install(), options=options)

        else:
            raise Exception("Selected browser not supported")