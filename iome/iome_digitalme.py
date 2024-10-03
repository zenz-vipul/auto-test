"""
    The code defines a class for automating profile editing on IOMe website using Selenium, including
    logging in, filling profile information, and submitting changes based on predefined scenarios.
"""

import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class EditProfileAutomation:
    def __init__(self, driver):
        self.driver = driver

    def setup(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    # Click on "Go to app" button
    def click_go_to_app(self):
        try:
            go_to_app_button = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[span[text()='Go to app']]")
                )
            )
            go_to_app_button.click()
            print("Clicked 'Go to app' button.")
        except TimeoutException:
            print("Timed out waiting for the 'Go to app' button to load.")
            print(self.driver.page_source)
        except Exception as e:
            print(f"An error occurred while clicking the 'Go to app' button: {e}")

    # Test 1: Login with username and password
    def login(self, username, password):
        try:
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//input[@placeholder="Username"]')
                )
            )
            username_field.send_keys(username)

            password_field = self.driver.find_element(
                By.XPATH, '//input[@placeholder="Password"]'
            )
            password_field.send_keys(password)

            self.driver.find_element(By.XPATH, '//button[span[text()="Login"]]').click()

            WebDriverWait(self.driver, 10).until(EC.url_contains("digitalme"))
            print(
                f"Login successful with Username: {username} and Password: {password}"
            )
            return True
        except TimeoutException:
            print(f"Login timed out for Username: {username} and Password: {password}")
            return False
        except Exception as e:
            print(
                f"An error occurred during login for Username: {username} and Password: {password}: {e}"
            )
            return False

    def login_to_account(self, username, password):
        print(f"Logging in with Username: {username}")
        print(f"Logging in with Password: {password}")

        self.click_go_to_app()
        login_successful = self.login(username, password)
        if login_successful:
            self.close_modal_if_present()
        return login_successful

    # Test 2: Close the recovery phrase modal
    def close_modal_if_present(self):
        try:
            close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[@aria-label='Close' and @class='ant-modal-close']",
                    )
                )
            )
            close_button.click()
            print("Closed the recovery phrase modal.")
        except TimeoutException:
            print("No recovery phrase modal appeared.")
        except Exception as e:
            print(f"An error occurred while trying to close the modal: {e}")

    # Test 3: Click on "Edit Profile" button
    def click_edit_profile(self):
        try:
            edit_profile_button = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[span[text()='Edit Profile']]")
                )
            )
            edit_profile_button.click()
            print("Clicked 'Edit Profile' button.")
        except TimeoutException:
            print("Timed out waiting for the 'Edit Profile' button to load.")
            print(self.driver.page_source)
        except Exception as e:
            print(f"An error occurred while clicking the 'Edit Profile' button: {e}")
            
    # Generate random data for testing
    def generate_random_data(self):
        first_name = "".join(random.choices(string.ascii_lowercase, k=5)).capitalize()
        last_name = "".join(random.choices(string.ascii_lowercase, k=5)).capitalize()
        email = "".join(random.choices(string.ascii_lowercase, k=7)) + "@example.com"
        phone = "".join(random.choices(string.digits, k=10))
        return first_name, last_name, email, phone


    # Test 4: Fill in profile information
    def fill_profile_info(self, first_name="", last_name="", email="", phone=""):
        try:
            if first_name:
                first_name_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//input[@placeholder="What is your first name?"]')
                    )
                )
                first_name_field.send_keys(Keys.CONTROL + "a")
                first_name_field.send_keys(Keys.DELETE)
                first_name_field.send_keys(first_name)

            if last_name:
                last_name_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '(//input[@placeholder="What is your last name?"])[1]')
                    )
                )
                last_name_field.send_keys(Keys.CONTROL + "a")
                last_name_field.send_keys(Keys.DELETE)
                last_name_field.send_keys(last_name)

            if email:
                email_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '(//input[@placeholder="unique@rmail.com"])[1]')
                    )
                )
                email_field.send_keys(Keys.CONTROL + "a")
                email_field.send_keys(Keys.DELETE)
                email_field.send_keys(email)

            if phone:
                phone_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '(//input[@placeholder="Enter phone number"])[1]')
                    )
                )
                phone_field.send_keys(Keys.CONTROL + "a")
                phone_field.send_keys(Keys.DELETE)
                phone_field.send_keys(phone)

        except Exception as e:
            print(f"An error occurred while filling profile information: {e}")

    # Test 5: Submit the profile
    def submit_profile(self):
        try:
            save_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[span[text()='Save information']]")
                )
            )
            save_button.click()
            print("Profile information submitted.")

            # Wait for modal to close if it appears
            # WebDriverWait(self.driver, 10).until(
            #     EC.invisibility_of_element_located(
            #         (By.XPATH, "//div[@class='ant-modal-wrap ant-modal-centered']")
            #     )
            # )

        except TimeoutException:
            print(
                "Timed out waiting for the 'Save information' button to become clickable."
            )
        except Exception as e:
            print(f"An error occurred while submitting profile: {e}")

    # Test 6: Fill in bio information
    def fill_bio(self, bio_text):
        try:
            bio_textarea = self.driver.find_element(
                By.XPATH, '//textarea[@placeholder="Bio"]'
            )
            bio_textarea.clear()
            bio_textarea.send_keys(bio_text)
            print("Filled in bio information.")
        except Exception as e:
            print(f"An error occurred while filling in the bio: {e}")


def main():
    driver = webdriver.Chrome()
    profile_test = EditProfileAutomation(driver)
    profile_test.setup("https://iome.ai")

    # Log in with specific credentials
    username = "VJ-108"
    password = "Test@123"
    profile_test.login_to_account(username, password)

    # Generate multiple scenarios using the random data
    scenarios = []
    for _ in range(5):
        random_data = profile_test.generate_random_data()
        scenarios.append(
            {
                "first_name": random_data[0],
                "last_name": random_data[1],
                "email": random_data[2],
                "phone": random_data[3],
                "bio": "This is a random bio.",
            }
        )

    # Test the scenarios
    for scenario in scenarios:
        profile_test.click_edit_profile()
        profile_test.fill_profile_info(
            first_name=scenario["first_name"],
            last_name=scenario["last_name"],
            email=scenario["email"],
            phone=scenario["phone"],
        )
        profile_test.fill_bio(scenario["bio"])
        profile_test.submit_profile()
        driver.refresh()
        profile_test.close_modal_if_present()

    driver.quit()


if __name__ == "__main__":
    main()
