import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.main_page import MainPage
from locators.main_locators import MainLocators

text_answer_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
text_answer_2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
text_answer_3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
text_answer_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
text_answer_5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
text_answer_6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
text_answer_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
text_answer_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


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
        assert WebDriverWait(driver, 5).until(ec.visibility_of_element_located(MainLocators.button_to_find))

    @allure.title('Проверка перехода на главную страницу "Самокат"')
    @allure.description('Проверяем переход на главную странцу "Самокат" из оформления заказа')
    def test_transition_to_scooter(self, driver):
        with allure.step('Кликаем на кнопку согласия "да все привыкли"'):
            MainPage(driver).clicking_button_cookies()
        with allure.step('Кликаем на верхнюю кнопкку "Заказать"'):
            MainPage(driver).clicking_order_top()
        with allure.step('Кликаем на логотип "САМОКАТ"'):
            MainPage(driver).clicking_logo_scooter()
        assert WebDriverWait(driver, 5).until(ec.visibility_of_element_located(MainLocators.main_inscription))

    @allure.title('Проверка выпадающих ответов на вопросы о важном')
    @allure.description('Проверяем, что при клике на вопросы о важном 1-8 будут развёрнуты ответы')
    @pytest.mark.parametrize('question, answer, right_answer',
                             [
                                 (MainLocators.question_1, MainLocators.answer_1, text_answer_1),
                                 (MainLocators.question_2, MainLocators.answer_2, text_answer_2),
                                 (MainLocators.question_3, MainLocators.answer_3, text_answer_3),
                                 (MainLocators.question_4, MainLocators.answer_4, text_answer_4),
                                 (MainLocators.question_5, MainLocators.answer_5, text_answer_5),
                                 (MainLocators.question_6, MainLocators.answer_6, text_answer_6),
                                 (MainLocators.question_7, MainLocators.answer_7, text_answer_7),
                                 (MainLocators.question_8, MainLocators.answer_8, text_answer_8)
                             ])
    def test_answers_to_questions(self, question, answer, right_answer, driver):
        with allure.step('Кликаем на кнопку согласия "да все привыкли"'):
            MainPage(driver).clicking_button_cookies()
        with allure.step('Скроллем страницу до 8-ого вопроса о важном'):
            MainPage(driver).find_questions()
        with allure.step('Дожидаемся видимости вопроса о важном и кликаем на него'):
            WebDriverWait(driver, 5).until(ec.visibility_of_element_located(question)).click()
        with allure.step('Дожидаемся видимости ответа на вопрос'):
            WebDriverWait(driver, 5).until(ec.visibility_of_element_located(answer))
        with allure.step('Берём текст найденного ответа'):
            right_text = driver.find_element(*answer).text
        assert right_text == right_answer
