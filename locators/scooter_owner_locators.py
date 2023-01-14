from selenium.webdriver.common.by import By


class ScooterOwnerLocators:

    button_further = [By.XPATH, "//button[contains(text(),'Далее')]"]  # Кнопка "Далее"
    name_input_field = [By.XPATH, "//*[@placeholder='* Имя']"]  # Поле ввода "Имя"
    lastname_input_field = [By.XPATH, "//*[@placeholder='* Фамилия']"]  # Поле ввода "Фамилия"
    address_input_field = [By.XPATH, "//*[@placeholder='* Адрес: куда привезти заказ']"]  # Поле ввода "Адрес"
    metro_sokolniki = [By.XPATH, "//*[@data-index='3']"]  # Метро"Сокольники"
    metro_sokol = [By.XPATH, "//*[@data-index='25']"]  # Метро"Сокол"
    station_selection_field = [By.XPATH, "//*[@class='select-search__input']"]  # Поле выбора станции
    phone_input_field = [By.XPATH, "//*[@placeholder='* Телефон: на него позвонит курьер']"]  # Поле ввода "Телефон"
