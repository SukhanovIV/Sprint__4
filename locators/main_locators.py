from selenium.webdriver.common.by import By


class MainLocators:

    button_to_find = [By.XPATH, "//*[@type='submit']"]  # Кнопка "Найти" на новой вкладке
    button_cookies = [By.XPATH, "//*[@id='rcc-confirm-button']"]  # Кнопка "да все привыкли" для согласия на куки-файлы
    logo_yandex = [By.XPATH, "//*[@alt='Yandex']"]  # Логотип "Яндекса"
    logo_scooter = [By.XPATH, "//*[@alt='Scooter']"]  # Логотип "Самоката"
    main_inscription = [By.XPATH, "//*[contains (@class, 'Home_SubHeader') and contains(text(), 'Привезём его')]"]  # Надпись "Привезём его прямо к вашей двери, а когда накатаетесь — заберём"
    order_top = [By.XPATH, "//*[contains(@class, 'Header_Nav')]/button[text() = 'Заказать']"]  # Кнопка "Заказать" сверху
    order_down = [By.XPATH, "//*[contains(@class, 'Home_FinishButton')]/button[text() = 'Заказать']"]  # Кнопка "Заказать" снизу
    question_1 = [By.XPATH, "//*[@id='accordion__heading-0']"]  # "Сколько это стоит? И как оплатить?"
    question_2 = [By.XPATH, "//*[@id='accordion__heading-1']"]  # "Хочу сразу несколько самокатов! Так можно?"
    question_3 = [By.XPATH, "//*[@id='accordion__heading-2']"]  # "Как рассчитывается время аренды?"
    question_4 = [By.XPATH, "//*[@id='accordion__heading-3']"]  # "Можно ли заказать самокат прямо на сегодня?"
    question_5 = [By.XPATH, "//*[@id='accordion__heading-4']"]  # "Можно ли продлить заказ или вернуть самокат раньше?"
    question_6 = [By.XPATH, "//*[@id='accordion__heading-5']"]  # "Вы привозите зарядку вместе с самокатом?"
    question_7 = [By.XPATH, "//*[@id='accordion__heading-6']"]  # "Можно ли отменить заказ?"
    question_8 = [By.XPATH, "//*[@id='accordion__heading-7']"]  # "Я живу за МКАДом, привезёте?"

    answer_1 = [By.XPATH,
                "//p[contains(text(),'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')]"]  # Ответ на 1 вопрос
    answer_2 = [By.XPATH,
                "//p[contains(text(),'Пока что у нас так: один заказ — один самокат. Если')]"]  # Ответ на 2 вопрос
    answer_3 = [By.XPATH,
                "//p[contains(text(),'Допустим, вы оформляете заказ на 8 мая. Мы привози')]"]  # Ответ на 3 вопрос
    answer_4 = [By.XPATH,
                "//p[contains(text(),'Только начиная с завтрашнего дня. Но скоро станем ')]"]  # Ответ на 4 вопрос
    answer_5 = [By.XPATH,
                "//p[contains(text(),'Пока что нет! Но если что-то срочное — всегда можн')]"]  # Ответ на 5 вопрос
    answer_6 = [By.XPATH,
                "//p[contains(text(),'Самокат приезжает к вам с полной зарядкой. Этого х')]"]  # Ответ на 6 вопрос
    answer_7 = [By.XPATH,
                "//p[contains(text(),'Да, пока самокат не привезли. Штрафа не будет, объ')]"]  # Ответ на 7 вопрос
    answer_8 = [By.XPATH,
                "//p[contains(text(),'Да, обязательно. Всем самокатов! И Москве, и Моско')]"]  # Ответ на 8 вопрос
