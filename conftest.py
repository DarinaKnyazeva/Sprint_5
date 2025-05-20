import random
import string

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def generate_random_email():
    random_string = ''.join(random.choices(string.ascii_lowercase, k=10))
    random_domain = ''.join(random.choices(string.ascii_lowercase, k=2))
    random_tld = random.choice(['com', 'ru'])
    email = f"{random_string}@{random_domain}.{random_tld}"
    return email

@pytest.fixture
def save_random_email(generate_random_email):
    correct_email = generate_random_email
    return correct_email

@pytest.fixture
def driver():
    driver_instance = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver_instance