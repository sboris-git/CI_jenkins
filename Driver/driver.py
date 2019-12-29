from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager


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

    def set_browser(self):
        if self.browser.lower() == "firefox":
            return webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif self.browser.lower() == "chrome":
            return webdriver.Chrome(ChromeDriverManager().install())
        elif self.browser.lower() == "ie":
            return webdriver.Ie(IEDriverManager().install())
        else:
            raise Exception("Selected browser not supported")