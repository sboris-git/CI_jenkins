from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import random


class BaseSetup:

    def __init__(self, event):
        self.driver = event


    def get_page_title(self):
        return self.driver.title

    def find_element(self, *locators):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(lambda driver: self.driver.find_element(*locators))
        return element

    def find_elements(self, *locators):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(lambda driver: self.driver.find_elements(*locators))
        return element

    def find_element_by_tag(self, tag):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(lambda driver: self.driver.find_elements_by_tag_name(tag))
        return element

    def find_element_by_xpath(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(lambda driver: self.driver.find_element_by_xpath(xpath))
        return element


    def get_list_element(self, ele_html: str, *locators):
        """get list of elements li, tr ....
            Args: locator = tuple(By.selector, 'str')
        """
        wait = WebDriverWait(self.driver, 10)
        lst = (list(lst_cat.get_attribute(ele_html)for lst_cat in
                    wait.until(EC.visibility_of_all_elements_located(*locators))))
        return lst

    def select_from_list(self, locator_1):
        sel = Select(self.find_element(*locator_1))
        choice = random.choice([c.text for c in sel.options])
        return choice

    def click_action(self, x, y):
        action = ActionChains(self.driver)
        action.move_by_offset(x, y).click().perform()


    def element_be_clickable(self, *locator):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.element_to_be_clickable(*locator))
            return element
        except TimeoutException as e:
            print('Element is not clickable')
            return ''

    def click_on_element(self, locators):
        element = self.find_element(*locators)
        element.click()

    def scroll_to_element(self, locators):
        #doesn't scroll by search element
        element = self.find_element(*locators)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()


    def clean_element(self, locators):
        element = self.find_element(*locators)
        element.clear()


    def send_keys_to_element(self, locators, data):
        element = self.find_element(*locators)
        element.send_keys(data)

    def upload_file(self, path, locators):
        element = self.find_element(locators)
        element.send_keys(path)

    def get_element_text(self, locator):
        element = self.find_element(*locator)
        print(element.text)
        return element.text

    # check if text present in element. Return True or print message
    def check_if_text_present(self, *locators, text=None):
        ''' Usage:
        self.error_str = "Failed"
        self.assertTrue(self.exec.base.check_if_text_present(self.locator.MES, self.error_str)), "not equal"

        where locator locator.MES is MES = (By.CSS_SELECTOR, 'css_string')'''

        error_msg = "Text not found"
        try:
            wait = WebDriverWait(self.driver, 5)
            text_get = wait.until(EC.text_to_be_present_in_element(*locators), text)
            return text_get
        except TimeoutException:
            print(error_msg)
            return ''

    def check_if_element_exists(self, locator, timeout=5):
        ''' Check the text attribute for an element as a criteria of existence.
        Args: locator = tuple(By.selector, 'str')
              waiting time = 10 # int()
        Returns text of element on success within timeout interval or
        an empty string and print a message for a raised exception.
        Explicit Waits method is used.
        '''

        alert = f"Can't find element by locator {locator}"
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                                message=alert)
            text_get = element.text
            return text_get
        except TimeoutException:
            print(alert)
            return None












