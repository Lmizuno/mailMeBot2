from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests
import bs4
import json
import os


# path = os.path.abspath('user_info.json')
# path = ('./../../user_info.json')
rel_path = """./../../user_info.json"""
script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0]
# ^-- absolute dir the script is in
abs_file_path = os.path.join(script_dir, rel_path)
with open(abs_file_path) as f:
    browserInfo = json.loads(f.read())


def getRequest():
    res = requests.get(browserInfo['scrapping-url-request'])
    res.raise_for_status()
    return res


def parseJsonToString(text):
    soup = bs4.BeautifulSoup(text, 'html.parser')
    info_json = json.loads(soup.get_text())
    body_text = info_json['body']['und'][0]['safe_value']
    return body_text


def getTextFromFindAll(text, tag):
    soup = bs4.BeautifulSoup(text, 'html.parser')
    answer = soup.find_all(tag)
    temp_list = []
    for index in answer:
        temp_list.append(index.get_text())
    return temp_list


def openBrowser():
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options, executable_path=browserInfo['gecko-driver-path'])
    browser.get(browserInfo['scrapping-url-selenium'])
    return browser


def fireIFTTT(date, update):
    data = {'value1': date, 'value2': update}
    requests.post(
        browserInfo['IFTTT-web-hook'], json=data)
