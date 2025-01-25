from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def fetch_car_details(registration_number):
    """Fetch car details from a valuation website."""
    driver = webdriver.Chrome()  # Ensure chromedriver is installed and in PATH
    url = "https://motorway.co.uk/"
    driver.get(url)
    time.sleep(2)

    # Locate search input and submit the registration number
    input_field = driver.find_element(By.NAME, "registration")
    input_field.send_keys(registration_number)
    input_field.send_keys(Keys.RETURN)
    time.sleep(5)

    # Extract car details (mocked example for simplicity)
    details = {
        "registration": registration_number,
        "make": driver.find_element(By.ID, "make").text,
        "model": driver.find_element(By.ID, "model").text,
        "year": driver.find_element(By.ID, "year").text,
    }

    driver.quit()
    return details

