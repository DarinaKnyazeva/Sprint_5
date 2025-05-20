from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import generate_random_email, save_random_email, driver
from locators import registration_button, non_account_button, registration_password_input, \
    registration_submitPassword_input, account_user_name, user_img, registration_email_input, submit_button, \
    log_out_button


class TestUserLogOut:

    def test_user_log_out(self, driver, generate_random_email, save_random_email):
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

        user_name = driver.find_elements(By.XPATH, account_user_name)
        img = driver.find_elements(By.XPATH, user_img)

        assert driver.find_element(By.XPATH, registration_button).text == 'Вход и регистрация'
        assert len(user_name) == 0
        assert len(img) == 0

        driver.quit()
