from Locators.locators import CartPanelsAtProfilePageLocators


class EventsMenuCarts:
    ''' Page object element for events carts panel: CartPanelsAtProfilePageLocators '''

    def __init__(self, browser):
        self.locator = CartPanelsAtProfilePageLocators.locators_dict
        self.browser = browser

    def element_at_menu_bar_is_present(self, item_name, timeout):
        ''' Check the text attribute for an element as a criteria of existence '''
        result = self.browser.check_if_element_exists(self.locator[item_name], timeout)
        if result is not None:
            return True