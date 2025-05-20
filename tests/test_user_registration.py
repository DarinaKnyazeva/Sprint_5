import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import generate_random_email, save_random_email, driver
from locators import registration_button, non_account_button, registration_password_input, \
    registration_submitPassword_input, account_user_name, user_img, registration_email_input, submit_button, \
    email_validation_error, log_out_button


class TestRegistrationUser:

    def test_user_registration(self, driver, generate_random_email):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        driver.find_element(By.XPATH, registration_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, non_account_button)))

        driver.find_element(By.XPATH, non_account_button).click()

        driver.find_element(By.XPATH, registration_email_input).send_keys(generate_random_email)
        driver.find_element(By.XPATH, registration_password_input).send_keys("123")
        driver.find_element(By.XPATH, registration_submitPassword_input).send_keys("123")

        driver.find_element(By.XPATH, submit_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, user_img)))

        user_name = driver.find_element(By.XPATH, account_user_name).text
        img = driver.find_elements(By.XPATH, user_img)

        assert driver.current_url == 'https://qa-desk.stand.praktikum-services.ru/regiatration'
        assert user_name == "User."
        assert len(img) == 1

        driver.quit()

    def test_registration_with_invalid_email(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        driver.find_element(By.XPATH, registration_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, non_account_button)))

        driver.find_element(By.XPATH, non_account_button).click()

        driver.find_element(By.XPATH, registration_email_input).send_keys(
            ''.join(random.choices(string.ascii_lowercase, k=10)))
        driver.find_element(By.XPATH, registration_password_input).send_keys("123")
        driver.find_element(By.XPATH, registration_submitPassword_input).send_keys("123")

        driver.find_element(By.XPATH, submit_button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, email_validation_error)))

        error_text = driver.find_elements(By.XPATH, email_validation_error)
        error_elements = driver.find_element(By.CSS_SELECTOR, '.input_inputError__fLUP9')

        assert error_text[0].text == 'Ошибка'
        assert error_elements.value_of_css_property("border") == '1px solid rgb(255, 105, 114)'

        driver.quit()

    def test_registration_existing_user(self, driver, generate_random_email, save_random_email):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        driver.find_element(By.XPATH, registration_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, non_account_button)))

        driver.find_element(By.XPATH, non_account_button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, registration_email_input)))

        driver.find_element(By.XPATH, registration_email_input).send_keys(save_random_email)
        driver.find_element(By.XPATH, registration_password_input).send_keys("1234")
        driver.find_element(By.XPATH, registration_submitPassword_input).send_keys("1234")

        driver.find_element(By.XPATH, submit_button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, log_out_button)))

        driver.find_element(By.XPATH, log_out_button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, registration_button)))

        driver.find_element(By.XPATH, registration_button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, non_account_button)))

        driver.find_element(By.XPATH, non_account_button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, registration_email_input)))

        driver.find_element(By.XPATH, registration_email_input).send_keys(save_random_email)
        driver.find_element(By.XPATH, registration_password_input).send_keys("1234")
        driver.find_element(By.XPATH, registration_submitPassword_input).send_keys("1234")

        driver.find_element(By.XPATH, submit_button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, email_validation_error)))

        error_text = driver.find_elements(By.XPATH, email_validation_error)
        error_elements = driver.find_element(By.CSS_SELECTOR, '.input_inputError__fLUP9')

        assert error_text[0].text == 'Ошибка'
        assert error_elements.value_of_css_property("border") == '1px solid rgb(255, 105, 114)'

        driver.quit()
