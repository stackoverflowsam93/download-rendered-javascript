import argparse
from pprint import pprint
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options


def handler_from_url(url):
    options = Options()
    options.add_argument(
        "--user-agent=Mozilla/5.0 "
        "(Macintosh; Intel Mac OS X 10_13_6) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/73.0.3683.86 Safari/537.36"
    )
    options.headless = True
    browser = Firefox(
        executable_path="./geckodriver",
        options=options
    )

    browser.get(url)
    
    return BeautifulSoup(browser.page_source, "lxml")


parser = argparse.ArgumentParser(description=(
    '-u --url docs url'
))

parser.add_argument('-u', '--url', type=str)
args = parser.parse_args()

pprint(handler_from_url(args.url))