from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import generate_random_email, save_random_email, driver
from locators import registration_button, non_account_button, registration_password_input, \
    registration_submitPassword_input, account_user_name, user_img, registration_email_input, submit_button, \
    log_out_button, log_in_button


class TestUserLogIn:

    def test_user_log_in(self, driver, generate_random_email, save_random_email):
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
            expected_conditions.visibility_of_element_located((By.XPATH, registration_email_input)))

        driver.find_element(By.XPATH, registration_email_input).send_keys(save_random_email)
        driver.find_element(By.XPATH, registration_password_input).send_keys("1234")

        driver.find_element(By.XPATH, log_in_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, user_img)))

        user_name = driver.find_element(By.XPATH, account_user_name).text
        img = driver.find_elements(By.XPATH, user_img)

        assert driver.current_url == 'https://qa-desk.stand.praktikum-services.ru/login'
        assert user_name == "User."
        assert len(img) == 1

        driver.quit()
