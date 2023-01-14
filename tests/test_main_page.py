import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.main_page import MainPage
from locators.main_locators import MainLocators


class TestMainPage:

    @allure.title('Проверка перехода на страницу "Дзен"')
    @allure.description('Проверяем переход на странцу "Дзен" через логотип "ЯНДЕКС"')
    def test_transition_to_zen(self, driver):
        with allure.step('Кликаем на кнопку согласия "да все привыкли"'):
            MainPage(driver).clicking_button_cookies()
        with allure.step('Кликаем на логотип "ЯНДЕКС"'):
            MainPage(driver).clicking_logo_yandex()
        with allure.step('Меняем фокус на новую открутую вкладку'):
            driver.switch_to.window(driver.window_handles[1])
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainLocators.button_to_find))

    @allure.title('Проверка перехода на главную страницу "Самокат"')
    @allure.description('Проверяем переход на главную странцу "Самокат" из оформления заказа')
    def test_transition_to_scooter(self, driver):
        with allure.step('Кликаем на кнопку согласия "да все привыкли"'):
            MainPage(driver).clicking_button_cookies()
        with allure.step('Кликаем на верхнюю кнопкку "Заказать"'):
            MainPage(driver).clicking_order_top()
        with allure.step('Кликаем на логотип "САМОКАТ"'):
            MainPage(driver).clicking_logo_scooter()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainLocators.main_inscription))

    @allure.title('Проверка выпадающего ответа на вопрос о важном №1')
    @allure.description('Проверяем, что при клике на вопрос о важном №1 будет развёрнут ответ')
    def test_answer_to_1_question(self, driver):
        with allure.step('Кликаем на кнопку согласия "да все привыкли"'):
            MainPage(driver).clicking_button_cookies()
        with allure.step('Скроллем страницу до 8-ого вопроса о важном'):
            MainPage(driver).find_questions()
        with allure.step('Дожитдаемся видимости последнего вопроса о важном'):
            WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainLocators.question_8))
        with allure.step('Кликаем на 1-ый вопрос о важном'):
            MainPage(driver).clicking_question_1()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainLocators.answer_1))

    @allure.title('Проверка выпадающего ответа на вопрос о важном №2')
    @allure.description('Проверяем, что при клике на вопрос о важном №2 будет развёрнут ответ')
    def test_answer_to_2_question(self, driver):
        with allure.step('Кликаем на кнопку согласия "да все привыкли"'):
            MainPage(driver).clicking_button_cookies()
        with allure.step('Скроллем страницу до 8-ого вопроса о важном'):
            MainPage(driver).find_questions()
        with allure.step('Дожитдаемся видимости последнего вопроса о важном'):
            WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainLocators.question_8))
        with allure.step('Кликаем на 2-ой вопрос о важном'):
            MainPage(driver).clicking_question_2()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainLocators.answer_2))

    @allure.title('Проверка выпадающего ответа на вопрос о важном №3')
    @allure.description('Проверяем, что при клике на вопрос о важном №3 будет развёрнут ответ')
    def test_answer_to_3_question(self, driver):
        with allure.step('Кликаем на кнопку согласия "да все привыкли"'):
            MainPage(driver).clicking_button_cookies()
        with allure.step('Скроллем страницу до 8-ого вопроса о важном'):
            MainPage(driver).find_questions()
        with allure.step('Дожитдаемся видимости последнего вопроса о важном'):
            WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainLocators.question_8))
        with allure.step('Кликаем на 3-ий вопрос о важном'):
            MainPage(driver).clicking_question_3()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainLocators.answer_3))

    @allure.title('Проверка выпадающего ответа на вопрос о важном №4')
    @allure.description('Проверяем, что при клике на вопрос о важном №4 будет развёрнут ответ')
    def test_answer_to_4_question(self, driver):
        with allure.step('Кликаем на кнопку согласия "да все привыкли"'):
            MainPage(driver).clicking_button_cookies()
        with allure.step('Скроллем страницу до 8-ого вопроса о важном'):
            MainPage(driver).find_questions()
        with allure.step('Дожитдаемся видимости последнего вопроса о важном'):
            WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainLocators.question_8))
        with allure.step('Кликаем на 4-ый вопрос о важном'):
            MainPage(driver).clicking_question_4()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainLocators.answer_4))

    @allure.title('Проверка выпадающего ответа на вопрос о важном №5')
    @allure.description('Проверяем, что при клике на вопрос о важном №5 будет развёрнут ответ')
    def test_answer_to_5_question(self, driver):
        with allure.step('Кликаем на кнопку согласия "да все привыкли"'):
            MainPage(driver).clicking_button_cookies()
        with allure.step('Скроллем страницу до 8-ого вопроса о важном'):
            MainPage(driver).find_questions()
        with allure.step('Дожитдаемся видимости последнего вопроса о важном'):
            WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainLocators.question_8))
        with allure.step('Кликаем на 5-ый вопрос о важном'):
            MainPage(driver).clicking_question_5()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainLocators.answer_5))

    @allure.title('Проверка выпадающего ответа на вопрос о важном №6')
    @allure.description('Проверяем, что при клике на вопрос о важном №6 будет развёрнут ответ')
    def test_answer_to_6_question(self, driver):
        with allure.step('Кликаем на кнопку согласия "да все привыкли"'):
            MainPage(driver).clicking_button_cookies()
        with allure.step('Скроллем страницу до 8-ого вопроса о важном'):
            MainPage(driver).find_questions()
        with allure.step('Дожитдаемся видимости последнего вопроса о важном'):
            WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainLocators.question_8))
        with allure.step('Кликаем на 6-ой вопрос о важном'):
            MainPage(driver).clicking_question_6()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainLocators.answer_6))

    @allure.title('Проверка выпадающего ответа на вопрос о важном №7')
    @allure.description('Проверяем, что при клике на вопрос о важном №7 будет развёрнут ответ')
    def test_answer_to_7_question(self, driver):
        with allure.step('Кликаем на кнопку согласия "да все привыкли"'):
            MainPage(driver).clicking_button_cookies()
        with allure.step('Скроллем страницу до 8-ого вопроса о важном'):
            MainPage(driver).find_questions()
        with allure.step('Дожитдаемся видимости последнего вопроса о важном'):
            WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainLocators.question_8))
        with allure.step('Кликаем на 7-ой вопрос о важном'):
            MainPage(driver).clicking_question_7()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainLocators.answer_7))

    @allure.title('Проверка выпадающего ответа на вопрос о важном №8')
    @allure.description('Проверяем, что при клике на вопрос о важном №8 будет развёрнут ответ')
    def test_answer_to_8_question(self, driver):
        with allure.step('Кликаем на кнопку согласия "да все привыкли"'):
            MainPage(driver).clicking_button_cookies()
        with allure.step('Скроллем страницу до 8-ого вопроса о важном'):
            MainPage(driver).find_questions()
        with allure.step('Дожитдаемся видимости последнего вопроса о важном'):
            WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainLocators.question_8))
        with allure.step('Кликаем на 8-ой вопрос о важном'):
            MainPage(driver).clicking_question_8()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainLocators.answer_8))
