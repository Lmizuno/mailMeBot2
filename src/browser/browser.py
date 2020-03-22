from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests
import bs4


def getRequest():
    res = requests.get('https://api.ontario.ca/api/drupal/page%2F2020-ontario-immigrant-nominee-program-updates?fields=nid,field_body_beta,body')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')


def openBrowser():
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options, executable_path=r'C:\\Python\\OinpApp\\geckodriver.exe')
    browser.get('https://www.ontario.ca/page/2020-ontario-immigrant-nominee-program-updates')
    return browser

