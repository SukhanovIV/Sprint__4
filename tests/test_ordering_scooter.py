import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.main_page import MainPage
from pages.scooter_owner_page import ScooterOwnerPage
from pages.rent_page import RentPage
from locators.rent_locators import RentLocators
from locators.main_locators import MainLocators


class TestOrderingScooter:

    @allure.title('Проверка заказа через верхнюю кнопку "Заказать"')
    @allure.description('Заказываем самокат через верхнюю кнопку "Заказать" при помощи примера из фикстуры 1, и проверяем, что заказ сформирован')
    def test_order_via_the_top_button(self, driver, example_1):
        with allure.step('Кликаем на кнопку согласия "да все привыкли"'):
            MainPage(driver).clicking_button_cookies()
        with allure.step('Кликаем на верхнюю кнопкку "Заказать"'):
            MainPage(driver).clicking_order_top()
        with allure.step('Заполняем страницу "Для кого самокат" данными примера 1'):
            ScooterOwnerPage(driver).enter_example_1(example_1)
        with allure.step('Кликаем на кнопкку "Далее"'):
            ScooterOwnerPage(driver).clicking_button_further()
        with allure.step('Дожитдаемся видимости кнопки "Заказать"'):
            WebDriverWait(driver, 20).until(ec.visibility_of_element_located(RentLocators.order))
        with allure.step('Выбор данных об аренде 1'):
            RentPage(driver).rental_option_1()
        with allure.step('Дожитдаемся видимости кнопки "Да", для подтверждения заказа'):
            WebDriverWait(driver, 20).until(ec.visibility_of_element_located(RentLocators.button_yes))
        with allure.step('Кликаем на кнопку "ДА", подтверждая заказ'):
            RentPage(driver).clicking_button_yes()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(RentLocators.view_status))

    @allure.title('Проверка заказа через нижнюю кнопку "Заказать"')
    @allure.description('Заказываем самокат через нижнюю кнопку "Заказать" при помощи примера из фикстуры 2, и проверяем, что заказ сформирован')
    def test_order_via_the_down_button(self, driver, example_2):
        with allure.step('Кликаем на кнопку согласия "да все привыкли"'):
            MainPage(driver).clicking_button_cookies()
        with allure.step('Скроллем страницу до 8-ого вопроса о важном'):
            MainPage(driver).find_questions()
        with allure.step('Дожитдаемся видимости нижней кнопки "Заказать"'):
            WebDriverWait(driver, 100).until(ec.visibility_of_element_located(MainLocators.order_down))
        with allure.step('Кликаем на нижнюю кнопкку "Заказать"'):
            MainPage(driver).clicking_order_down()
        with allure.step('Заполняем страницу "Для кого самокат" данными примера 2'):
            ScooterOwnerPage(driver).enter_example_2(example_2)
        with allure.step('Кликаем на кнопкку "Далее"'):
            ScooterOwnerPage(driver).clicking_button_further()
        with allure.step('Дожитдаемся видимости кнопки "Заказать"'):
            WebDriverWait(driver, 20).until(ec.visibility_of_element_located(RentLocators.order))
        with allure.step('Выбор данных об аренде 2'):
            RentPage(driver).rental_option_2()
        with allure.step('Дожитдаемся видимости кнопки "Да", для подтверждения заказа'):
            WebDriverWait(driver, 20).until(ec.visibility_of_element_located(RentLocators.button_yes))
        with allure.step('Кликаем на кнопку "ДА", подтверждая заказ'):
            RentPage(driver).clicking_button_yes()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(RentLocators.view_status))
