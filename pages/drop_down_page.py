from locators.drop_down_locators import DropDownLocators


class DropDownPage:

    def __init__(self, driver):
        self.driver = driver

    def clicking_question_1(self):
        self.driver.find_element(*DropDownLocators.question_1).click()

    def clicking_question_2(self):
        self.driver.find_element(*DropDownLocators.question_2).click()

    def clicking_question_3(self):
        self.driver.find_element(*DropDownLocators.question_3).click()

    def clicking_question_4(self):
        self.driver.find_element(*DropDownLocators.question_4).click()

    def clicking_question_5(self):
        self.driver.find_element(*DropDownLocators.question_5).click()

    def clicking_question_6(self):
        self.driver.find_element(*DropDownLocators.question_6).click()

    def clicking_question_7(self):
        self.driver.find_element(*DropDownLocators.question_7).click()

    def clicking_question_8(self):
        self.driver.find_element(*DropDownLocators.question_8).click()

    def find_questions(self):
        element = self.driver.find_element(*DropDownLocators.question_8)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
