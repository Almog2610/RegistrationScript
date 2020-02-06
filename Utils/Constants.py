from time import gmtime, strftime

# Web Driver Constants
HASTE_WEBSITE_URL = "https://haste.net"
HASTE_FREE_TRIAL_URL = "https://account.haste.net/my-account/?hm=register"
FAKE_EMAIL_URL = "http://www.fakemailgenerator.com/"
CHROME_DRIVER_PATH = "chromedriver.exe"
WEBSITE_AFTER_SIGNUP_DELAY_IN_MSEC = 120

# Name generator constants
NAMES_SIZE = 2818
RANDOM_START_INPUT = 0
RANDOM_NAMES_FILE_NAME = "RandomNames.txt"
RANDOM_NAMES_FILE_PATH = "Utils/RandomNames.txt"
FILE_READING_MODE = 'r'

# File User file constants
HASTE_USER_FILE_PATH = ".."
HASTE_USER_FILE_NAME = "Haste_user_file" + strftime("%H:%M:%S %d-%m-%Y", gmtime())

# Email Generator constants
FAKE_EMAIL_REFRESH_URL = "https://emailfake.com/fake_email_generator"
