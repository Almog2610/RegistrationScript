from selenium import webdriver
from time import sleep

from Generators.EmailGenerator import EmailGenerator
from Generators.HasteUserGenerator import HasteUserGenerator
from Utils import Constants
import WebDriver


def main():
    browser = webdriver.Chrome(Constants.CHROME_DRIVER_PATH)
    browser.get(Constants.HASTE_FREE_TRIAL_URL)

    email_generator = EmailGenerator()
    haste_user_generator = HasteUserGenerator()

    user_data = haste_user_generator.generate_user(email_generator)

    WebDriver.fill_input_boxes(browser, user_data)
    WebDriver.click_sign_up_button(browser, button_id="register")

    sleep(Constants.WEBSITE_AFTER_SIGNUP_DELAY_IN_MSEC)

    haste_user_generator.create_user_file(Constants.HASTE_USER_FILE_PATH, Constants.HASTE_USER_FILE_NAME)

    # email_generator.confirm_email()

    input("Press enter to continue...")


if __name__ == '__main__':
    main()
