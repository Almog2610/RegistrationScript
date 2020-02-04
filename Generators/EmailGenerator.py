# region Imports

from selenium import webdriver
from Utils import Constants


# endregion

class EmailGenerator:

    # region Functions

    def __init__(self, browser=None):
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
        try:
            email_web_element = self.browser.find_element_by_id("email_ch_text")

        except Exception as exception:
            print(exception)

        return email_web_element.text

    def confirm_email(self):
        confirm_button = self.browser.find_element_by_class_name("mcnButton")
        confirm_button.click()

    # endregion
