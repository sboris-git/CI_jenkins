from Base.base import BaseSetup
from Pages.POM.linkedin_page_tmp_boris import SignLinkedInClass


class InitPages():
    '''Instantiating a class by making a composition'''

    def __init__(self, driver_init):
        self.base = BaseSetup(driver_init)
        self.linked = SignLinkedInClass(self.base)
