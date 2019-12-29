from selenium.webdriver.common.by import By


class LoginPageLocators:
    '''ToDo Simulating
    from Locators.locators import LoginPageLocators'''

    EMAIL_SIGNIN = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    BUTTON_SIGIN = (By.CSS_SELECTOR, 'button[aria-label*="Sign"]')


class SignLinkedInClass():
    ''' ToDo boris' Temporary stub to debug the project without access to the eventExpress'''

    def __init__(self, browser):
        self.browser = browser
        self.locator = LoginPageLocators

    def type_login(self, login):
        self.browser.send_keys_to_element(self.locator.EMAIL_SIGNIN, login)

    def type_pass(self, password):
        self.browser.send_keys_to_element( self.locator.PASSWORD, password )

    def press_button_signin(self):
        self.browser.click_on_element(self.locator.BUTTON_SIGIN)

    @property
    def title(self):
        return self.browser.get_page_title()