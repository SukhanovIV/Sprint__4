import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class Example:
    def __init__(self, name, lastname, address, phone):
        self.name = name
        self.lastname = lastname
        self.address = address
        self.phone = phone


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    #options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()


@pytest.fixture
def example_1():
    return Example(name='Иван', lastname='Суханов', address='Москва, улица Фоничёвой, дом 4', phone='88005553535')


@pytest.fixture
def example_2():
    return Example(name='Владимир', lastname='Махов', address='Москва, улица Руставели, дом 7', phone='89997772525')
