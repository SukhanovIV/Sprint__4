from selenium.webdriver.common.by import By


class RentLocators:

    order = [By.XPATH, "//*[@class='Button_Button__ra12g Button_Middle__1CSJM']"]  # Кнопка "Заказать" финальная
    when_to_bring = [By.XPATH, "//*[@class='react-datepicker__input-container']"]  # Поле выбора даты
    january_20th = [By.XPATH, "//*[@class='react-datepicker__day react-datepicker__day--020']"]  # Дата 20 января
    january_26th = [By.XPATH, "//*[@class='react-datepicker__day react-datepicker__day--026']"]  # Дата 26 января
    rental_period = [By.XPATH, "//div[contains(text(),'* Срок аренды')]"]  # Поле срок аренды
    one_day = [By.XPATH, "(//*[@class='Dropdown-option'])[1]"]  # 1 сутки
    three_day = [By.XPATH, "(//*[@class='Dropdown-option'])[3]"]  # 3 суток
    black_color = [By.XPATH, "(//*[@class='Checkbox_Label__3wxSf'])[1]"]  # Чёрный цвет самоката
    grey_color = [By.XPATH, "(//*[@class='Checkbox_Label__3wxSf'])[2]"]  # Серый цвет самоката
    button_yes = [By.XPATH, "//*[@class='Button_Button__ra12g Button_Middle__1CSJM']"]  # Кнопка "Да", подтверждающая заказ
    view_status = [By.XPATH, "//*[@class='Button_Button__ra12g Button_Middle__1CSJM']"]  # Кнопка "Посмотреть статус" заказа
