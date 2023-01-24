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

    def find_questions(self):
        """ Скроллем страницу до 8-ого вопроса о важном """
        element = self.driver.find_element(*MainLocators.question_8)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
