from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.drop_down_page import DropDownPage
from locators.drop_down_locators import DropDownLocators


class TestDropDownPage:

    def test_answer_to_1_question(self, driver):
        page = DropDownPage(driver)
        page.find_questions()
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(DropDownLocators.question_8))
        page.clicking_question_1()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(DropDownLocators.answer_1))

    def test_answer_to_2_question(self, driver):
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(DropDownPage.find_questions(driver)))
        DropDownPage.clicking_question_2(driver)
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            DropDownLocators.answer_2))

    def test_answer_to_3_question(self, driver):
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(DropDownPage.find_questions(driver)))
        DropDownPage.clicking_question_3(driver)
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            DropDownLocators.answer_3))

    def test_answer_to_4_question(self, driver):
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(DropDownPage.find_questions(driver)))
        DropDownPage.clicking_question_4(driver)
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            DropDownLocators.answer_4))

    def test_answer_to_5_question(self, driver):
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(DropDownPage.find_questions(driver)))
        DropDownPage.clicking_question_5(driver)
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            DropDownLocators.answer_5))

    def test_answer_to_6_question(self, driver):
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(DropDownPage.find_questions(driver)))
        DropDownPage.clicking_question_6(driver)
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            DropDownLocators.answer_6))

    def test_answer_to_7_question(self, driver):
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(DropDownPage.find_questions(driver)))
        DropDownPage.clicking_question_7(driver)
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            DropDownLocators.answer_7))

    def test_answer_to_8_question(self, driver):
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(DropDownPage.find_questions(driver)))
        DropDownPage.clicking_question_8(driver)
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            DropDownLocators.answer_8))
