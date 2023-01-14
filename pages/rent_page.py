from locators.rent_locators import RentLocators


class RentPage:

    def __init__(self, driver):
        self.driver = driver

    def clicking_order(self):
        """ Кликаем на кнопкку "Заказать" """
        self.driver.find_element(*RentLocators.order).click()

    def clicking_when_to_bring(self):
        """ Кликаем на поле "Когда привезти самокат" """
        self.driver.find_element(*RentLocators.when_to_bring).click()

    def choice_january_20th(self):
        """ Выбираем дату - 20 января """
        self.driver.find_element(*RentLocators.when_to_bring).click()
        self.driver.find_element(*RentLocators.january_20th).click()

    def choice_january_26th(self):
        """ Выбираем дату - 26 января """
        self.driver.find_element(*RentLocators.when_to_bring).click()
        self.driver.find_element(*RentLocators.january_26th).click()

    def clicking_rental_period(self):
        """ Кликаем на поле "Срок аренды" """
        self.driver.find_element(*RentLocators.rental_period).click()

    def choice_one_day(self):
        """ Выбираем срок - "Сутки" """
        self.driver.find_element(*RentLocators.rental_period).click()
        self.driver.find_element(*RentLocators.one_day).click()

    def choice_three_day(self):
        """ Выбираем срок - "Трое суток" """
        self.driver.find_element(*RentLocators.rental_period).click()
        self.driver.find_element(*RentLocators.three_day).click()

    def clicking_black_color(self):
        """ Выбираем цвет самоката - "Чёрный жемчуг" """
        self.driver.find_element(*RentLocators.black_color).click()

    def clicking_grey_color(self):
        """ Выбираем цвет самоката - "серая безысходность" """
        self.driver.find_element(*RentLocators.grey_color).click()

    def clicking_button_yes(self):
        """ Кликаем на кнопку "ДА", подтверждая заказ """
        self.driver.find_element(*RentLocators.button_yes).click()

    def rental_option_1(self):
        """ Выбор данных об аренде 1 """
        self.choice_january_20th()
        self.choice_one_day()
        self.clicking_black_color()

    def rental_option_2(self):
        """ Выбор данных об аренде 2 """
        self.choice_january_26th()
        self.choice_three_day()
        self.clicking_grey_color()
