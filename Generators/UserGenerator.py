# region Imports

from random import randint
from Utils import Constants
import uuid

# endregion

# region Global variables

string_length = 10


# endregion


# region Functions

def generate_name():
    with open(Constants.RANDOM_NAMES_FILE_PATH, Constants.FILE_READING_MODE) as name_file:
        name_index = randint(Constants.RANDOM_START_INPUT, Constants.NAMES_SIZE)
        names = name_file.readlines()
        return names[name_index].rstrip('\n')


def generate_username():
    with open(Constants.RANDOM_NAMES_FILE_PATH, Constants.FILE_READING_MODE) as name_file:
        name_index = randint(Constants.RANDOM_START_INPUT, Constants.NAMES_SIZE)
        username = name_file.readlines()[name_index].rstrip('\n')
        username += str(randint(Constants.RANDOM_START_INPUT, Constants.NAMES_SIZE))
        return username


def generate_password():
    # Todo : check generated password
    password = uuid.uuid4().hex  # get a random string in a UUID format
    password = password[0:string_length]  # convert it in a uppercase letter and trim to your size.

    password = uuid.uuid4().hex
    password = password.lower()[0:string_length]

    return password

# endregion
