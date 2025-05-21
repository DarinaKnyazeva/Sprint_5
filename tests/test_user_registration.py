import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import generate_random_email, save_random_email, driver
from data import REGISTRATION_URL
from locators import REGISTRATION_BUTTON, NON_ACCOUNT_BUTTON, REGISTRATION_PASSWORD_INPUT, \
    REGISTRATION_SUBMIT_PASSWORD_INPUT, ACCOUNT_USER_NAME, USER_IMG, REGISTRATION_EMAIL_INPUT, SUBMIT_BUTTON, \
    EMAIL_VALIDATION_ERROR, LOG_OUT_BUTTON, ERROR_ELEMENTS


class TestRegistrationUser:

    def test_user_registration(self, driver, generate_random_email):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        driver.find_element(By.XPATH, REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, NON_ACCOUNT_BUTTON)))

        driver.find_element(By.XPATH, NON_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, REGISTRATION_EMAIL_INPUT)))

        driver.find_element(By.XPATH, REGISTRATION_EMAIL_INPUT).send_keys(generate_random_email)
        driver.find_element(By.XPATH, REGISTRATION_PASSWORD_INPUT).send_keys("123")
        driver.find_element(By.XPATH, REGISTRATION_SUBMIT_PASSWORD_INPUT).send_keys("123")

        driver.find_element(By.XPATH, SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, USER_IMG)))

        user_name = driver.find_element(By.XPATH, ACCOUNT_USER_NAME).text
        img = driver.find_elements(By.XPATH, USER_IMG)

        assert driver.current_url == REGISTRATION_URL
        assert user_name == "User."
        assert len(img) == 1

    def test_registration_with_invalid_email(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        driver.find_element(By.XPATH, REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, NON_ACCOUNT_BUTTON)))

        driver.find_element(By.XPATH, NON_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, REGISTRATION_EMAIL_INPUT)))

        driver.find_element(By.XPATH, REGISTRATION_EMAIL_INPUT).send_keys(
            ''.join(random.choices(string.ascii_lowercase, k=10)))
        driver.find_element(By.XPATH, REGISTRATION_PASSWORD_INPUT).send_keys("123")
        driver.find_element(By.XPATH, REGISTRATION_SUBMIT_PASSWORD_INPUT).send_keys("123")

        driver.find_element(By.XPATH, SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, EMAIL_VALIDATION_ERROR)))

        error_text = driver.find_elements(By.XPATH, EMAIL_VALIDATION_ERROR)
        error_elements = driver.find_element(By.CSS_SELECTOR, ERROR_ELEMENTS)

        assert error_text[0].text == 'Ошибка'
        assert error_elements.value_of_css_property("border") == '1px solid rgb(255, 105, 114)'

    def test_registration_existing_user(self, driver, generate_random_email, save_random_email):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        driver.find_element(By.XPATH, REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, NON_ACCOUNT_BUTTON)))

        driver.find_element(By.XPATH, NON_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, REGISTRATION_EMAIL_INPUT)))

        driver.find_element(By.XPATH, REGISTRATION_EMAIL_INPUT).send_keys(save_random_email)
        driver.find_element(By.XPATH, REGISTRATION_PASSWORD_INPUT).send_keys("1234")
        driver.find_element(By.XPATH, REGISTRATION_SUBMIT_PASSWORD_INPUT).send_keys("1234")

        driver.find_element(By.XPATH, SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, LOG_OUT_BUTTON)))

        driver.find_element(By.XPATH, LOG_OUT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, REGISTRATION_BUTTON)))

        driver.find_element(By.XPATH, REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, NON_ACCOUNT_BUTTON)))

        driver.find_element(By.XPATH, NON_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, REGISTRATION_EMAIL_INPUT)))

        driver.find_element(By.XPATH, REGISTRATION_EMAIL_INPUT).send_keys(save_random_email)
        driver.find_element(By.XPATH, REGISTRATION_PASSWORD_INPUT).send_keys("1234")
        driver.find_element(By.XPATH, REGISTRATION_SUBMIT_PASSWORD_INPUT).send_keys("1234")

        driver.find_element(By.XPATH, SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, EMAIL_VALIDATION_ERROR)))

        error_text = driver.find_elements(By.XPATH, EMAIL_VALIDATION_ERROR)
        error_elements = driver.find_element(By.CSS_SELECTOR, ERROR_ELEMENTS)

        assert error_text[0].text == 'Ошибка'
        assert error_elements.value_of_css_property("border") == '1px solid rgb(255, 105, 114)'
