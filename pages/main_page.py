from locators.main_locators import MainLocators


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def clicking_logo_yandex(self):
        """ Кликаем на логотип "ЯНДЕКС" """
        self.driver.find_element(*MainLocators.logo_yandex).click()

    def clicking_logo_scooter(self):
        """ Кликаем на логотип "САМОКАТ" """
        self.driver.find_element(*MainLocators.logo_scooter).click()

    def clicking_button_cookies(self):
        """ Кликаем на кнопку согласия куки "да все привыкли" """
        self.driver.find_element(*MainLocators.button_cookies).click()

    def clicking_order_top(self):
        """ Кликаем на верхнюю кнопкку "Заказать" """
        self.driver.find_element(*MainLocators.order_top).click()

    def clicking_order_down(self):
        """ Кликаем на нижнюю кнопкку "Заказать" """
        self.driver.find_element(*MainLocators.order_down).click()

    def clicking_question_1(self):
        """ Кликаем на 1-ый вопрос о важном """
        self.driver.find_element(*MainLocators.question_1).click()

    def clicking_question_2(self):
        """ Кликаем на 2-ой вопрос о важном """
        self.driver.find_element(*MainLocators.question_2).click()

    def clicking_question_3(self):
        """ Кликаем на 3-ий вопрос о важном """
        self.driver.find_element(*MainLocators.question_3).click()

    def clicking_question_4(self):
        """ Кликаем на 4-ый вопрос о важном """
        self.driver.find_element(*MainLocators.question_4).click()

    def clicking_question_5(self):
        """ Кликаем на 5-ый вопрос о важном """
        self.driver.find_element(*MainLocators.question_5).click()

    def clicking_question_6(self):
        """ Кликаем на 6-ой вопрос о важном """
        self.driver.find_element(*MainLocators.question_6).click()

    def clicking_question_7(self):
        """ Кликаем на 7-ой вопрос о важном """
        self.driver.find_element(*MainLocators.question_7).click()

    def clicking_question_8(self):
        """ Кликаем на 8-ой вопрос о важном """
        self.driver.find_element(*MainLocators.question_8).click()

    def find_questions(self):
        """ Скроллем страницу до 8-ого вопроса о важном """
        element = self.driver.find_element(*MainLocators.question_8)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
