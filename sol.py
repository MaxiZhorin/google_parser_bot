import json
from bs4 import BeautifulSoup
import requests
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import pandas as pd
from lxml import html


if __name__ == '__main__':
    url = 'https://www.google.com/search?q=scrapy'
    webdriver = '/usr/local/bin/chromedriver'
    chrome = Chrome(webdriver)
    chrome.get(url)
    elem =[]
    elem = chrome.find_elements_by_class_name("rc")
    print(len (elem))
    for i in elem:
        print(i.find_element_by_tag_name('a').get_attribute('href'))
        print('')