from bs4 import BeautifulSoup


def get_all_registration_input_types(website_data):
    input_types = get_all_input_types(website_data)
    print(input_types)


def get_all_input_types(website_data):
    input_types = website_data.find_all('input')
    return input_types
