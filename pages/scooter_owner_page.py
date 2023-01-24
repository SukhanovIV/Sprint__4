from locators.scooter_owner_locators import ScooterOwnerLocators


class ScooterOwnerPage:

    def __init__(self, driver):
        self.driver = driver

    def clicking_button_further(self):
        """ Кликаем на кнопкку "Далее" """
        self.driver.find_element(*ScooterOwnerLocators.button_further).click()

    def enter_name_1(self, example_1):
        """ Вводим в поле "ИМЯ" фикстуру имени 1 """
        self.driver.find_element(*ScooterOwnerLocators.name_input_field).send_keys(example_1.name)
        return example_1

    def enter_name_2(self, example_2):
        """ Вводим в поле "ИМЯ" фикстуру имени 2 """
        self.driver.find_element(*ScooterOwnerLocators.name_input_field).send_keys(example_2.name)
        return example_2

    def enter_lastname_1(self, example_1):
        """ Вводим в поле "ФАМИЛИЯ" фикстуру фамилии 1 """
        self.driver.find_element(*ScooterOwnerLocators.lastname_input_field).send_keys(example_1.lastname)
        return example_1

    def enter_lastname_2(self, example_2):
        """ Вводим в поле "ФАМИЛИЯ" фикстуру фамилии 2 """
        self.driver.find_element(*ScooterOwnerLocators.lastname_input_field).send_keys(example_2.lastname)
        return example_2

    def enter_address_1(self, example_1):
        """ Вводим в поле "АДРЕС" фикстуру адреса 1 """
        self.driver.find_element(*ScooterOwnerLocators.address_input_field).send_keys(example_1.address)
        return example_1

    def enter_address_2(self, example_2):
        """ Вводим в поле "АДРЕС" фикстуру адреса 2 """
        self.driver.find_element(*ScooterOwnerLocators.address_input_field).send_keys(example_2.address)
        return example_2

    def choice_station_sokolniki(self):
        """ Выбираем в поле "СТАНЦИЯ МЕТРО" станцию "Сокольники" """
        self.driver.find_element(*ScooterOwnerLocators.station_selection_field).click()
        self.driver.find_element(*ScooterOwnerLocators.metro_sokolniki).click()

    def choice_station_sokol(self):
        """ Выбираем в поле "СТАНЦИЯ МЕТРО" станцию "Сокол" """
        self.driver.find_element(*ScooterOwnerLocators.station_selection_field).click()
        self.driver.find_element(*ScooterOwnerLocators.metro_sokol).click()

    def enter_phone_1(self, example_1):
        """ Вводим в поле "ТЕЛЕФОН" фикстуру телефона 1 """
        self.driver.find_element(*ScooterOwnerLocators.phone_input_field).send_keys(example_1.phone)
        return example_1

    def enter_phone_2(self, example_2):
        """ Вводим в поле "ТЕЛЕФОН" фикстуру телефона 2 """
        self.driver.find_element(*ScooterOwnerLocators.phone_input_field).send_keys(example_2.phone)
        return example_2

    def enter_example_1(self, example_1):
        """ Заполняем страницу "Для кого самокат" данными примера 1 """
        self.enter_name_1(example_1)
        self.enter_lastname_1(example_1)
        self.enter_address_1(example_1)
        self.choice_station_sokolniki()
        self.enter_phone_1(example_1)
        return example_1

    def enter_example_2(self, example_2):
        """ Заполняем страницу "Для кого самокат" данными примера 2 """
        self.enter_name_2(example_2)
        self.enter_lastname_2(example_2)
        self.enter_address_2(example_2)
        self.choice_station_sokol()
        self.enter_phone_2(example_2)
        return example_2
