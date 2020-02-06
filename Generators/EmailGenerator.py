# region Imports

from selenium import webdriver
from Utils import Constants, UtilityFunctions
from time import sleep


# endregion

class EmailGenerator:

    # region Functions

    def __init__(self, browser=None):
        self.email_ready = False
        if browser is None:
            self.browser = webdriver.Chrome(Constants.CHROME_DRIVER_PATH)
        else:
            self.browser = browser

    def generate_email(self):
        self.open_fake_email_generator_web_page()
        return self.get_email()

    def open_fake_email_generator_web_page(self):
        self.browser.get(Constants.FAKE_EMAIL_URL)

    def get_email(self):
        email_web_element = None
        self.email_ready = False
        try:
            email_web_element = self.browser.find_element_by_id("cxtEmail")
            return email_web_element.text

        except Exception as exception:
            print("Cannot get email : " + exception.__str__())

    def confirm_email(self):
        confirm_button = self.browser.find_element_by_partial_link_text(
            "https://account.haste.net/my-account/?hm=validate")
        confirm_button.click()

    def refresh_fake_email(self):
        self.browser.get(Constants.FAKE_EMAIL_REFRESH_URL)

# endregion
