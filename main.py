from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from Utils import Constants


def main():
    header = {'User-Agent': 'Mozilla/5.0'}
    request = Request(Constants.HASTE_FREE_TRIAL_URL, headers=header)

    with urlopen(request) as html_page:
        html_page_data = html_page.read()
        haste_beautiful_soup = BeautifulSoup(html_page_data, features="html.parser")
        print(haste_beautiful_soup)


if __name__ == '__main__':
    main()
