from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
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

    @property
    def set_browser(self):

        if self.browser.lower() == "firefox":
            options = FirefoxOptions()
            options.headless = True
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_options=options)

        elif self.browser.lower() == "chrome":
            options = Options()
            options.headless = True
            # options.add_argument("headless")
            '''from selenium import webdriver
               from selenium.webdriver.chrome.options import Options
               options = Options()
               options.add_argument("no-sandbox")
               options.add_argument("start-maximized")
               options.add_argument("window-size=1900,1080"); 
               driver = webdriver.Chrome(chrome_options=options, executable_path="/usr/bin/chromedriver")'''
            # options.headless = True
            # options.add_argument('--headless')
            # options.add_argument('--disable-gpu')
            # options.add_argument("--no-sandbox")
            # options.add_argument("window-size=1400,2100")  # Linux should be activate
            return webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

        elif self.browser.lower() == "ie":
            return webdriver.Ie(IEDriverManager().install(), ie_options=options)

        else:
            raise Exception("Selected browser not supported")