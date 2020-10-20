# coding: utf-8
import json
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def get_json_list( url ):
    chrome.get(url)
    elem = []
    object_dict = {}
    elem = chrome.find_elements_by_class_name("rc")  # Находим элементы с название класа
    obj = 1
    for i in elem:
        name_object = i.text.split('\n')[0]  # Сплитуем первую строку из текста получаем имя объекта
        url_object = i.find_element_by_tag_name('a').get_attribute('href')  # Получаем ссылку на объект
        description_object = i.text.split('\n')
        if description_object.count('Перевести эту страницу'):
            description_object = description_object[3]
        else:
            description_object = description_object[2]
            if description_object.count('г. —'):
                description_object = description_object.split('г. — ')[1]  # Сплитуем нужное нам описание
        object_dict["object" + str(obj)] = {  # Создаем предварительный словарь
            'Name' : name_object,
            'Url' : url_object,
            'Description' : description_object
        }
        obj += 1
    with open('json_parse.json','w', encoding='utf-8') as file:  # Создаем json файл
        json.dump(object_dict, file, ensure_ascii=False)


if __name__ == '__main__':
    url = 'https://www.google.com/search?q=scrapy'  # Url для парсинга
    webdriver = '/usr/local/bin/chromedriver'  # Путь к файлу драйвера для selenium
    opts = Options()
    opts.set_headless()
    assert opts.headless  # Отключаем графический интерфейс
    chrome = Chrome(webdriver, options=opts)
    get_json_list( url )