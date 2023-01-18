from selenium.webdriver.common.by import By


class RentLocators:

    order = [By.XPATH, "(//*[contains (@class, 'Button_Button') and contains(text(), 'Заказать')])[2]"]  # Кнопка "Заказать" финальная
    when_to_bring = [By.XPATH, "//*[@placeholder='* Когда привезти самокат']"]  # Поле выбора даты
    january_20th = [By.XPATH, "//*[@aria-label='Choose пятница, 20-е января 2023 г.']"]  # Дата 20 января
    january_26th = [By.XPATH, "//*[@aria-label='Choose четверг, 26-е января 2023 г.']"]  # Дата 26 января
    rental_period = [By.XPATH, "//div[contains(text(),'* Срок аренды')]"]  # Поле срок аренды
    one_day = [By.XPATH, "(//*[@class='Dropdown-option'])[1]"]  # 1 сутки
    three_day = [By.XPATH, "(//*[@class='Dropdown-option'])[3]"]  # 3 суток
    black_color = [By.XPATH, "//*[@for='black']"]  # Чёрный цвет самоката
    grey_color = [By.XPATH, "//*[@for='grey']"]  # Серый цвет самоката
    button_yes = [By.XPATH, "//*[contains (@class, 'Button_Button') and contains(text(), 'Да')]"]  # Кнопка "Да", подтверждающая заказ
    view_status = [By.XPATH, "//*[contains (@class, 'Button_Button') and contains(text(), 'Посмотреть статус')]"]  # Кнопка "Посмотреть статус" заказа
