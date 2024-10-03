"""
    The script automates the process of logging into IOMe application using Selenium, generating random
    credentials for testing, and testing login with both scenarios and specific credentials.
"""

import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class AccountAutomation:
    def __init__(self, driver):
        self.driver = driver

    def setup(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    # Click on "Go to app" button
    def click_go_to_app(self):
        try:
            go_to_app_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[span[text()='Go to app']]")
                )
            )
            go_to_app_button.click()
        except TimeoutException:
            print("Timed out waiting for the 'Go to app' button to load.")
            print(self.driver.page_source)  # Print the page source to debug
        except Exception as e:
            print(f"An error occurred while clicking the 'Go to app' button: {e}")

    # Login with username and password
    def login(self, username, password):
        try:
            # Locate and clear username field
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

            WebDriverWait(self.driver, 20).until(EC.url_contains("digitalme"))
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

    # Generate random username and password
    def generate_random_credentials(self):
        username = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
        password = "".join(random.choices(string.ascii_letters + string.digits, k=10))
        return username, password

    # Workflow to login with existing credentials
    def login_to_account(self, username, password):
        print(f"Logging in with Username: {username}")
        print(f"Logging in with Password: {password}")

        self.click_go_to_app()
        return self.login(username, password)


# Test workflow
def main():
    driver = webdriver.Chrome()
    account = AccountAutomation(driver)
    account.setup("https://iome.ai")

    # Test with two random credentials
    for _ in range(1):
        random_username, random_password = account.generate_random_credentials()
        print(
            f"Testing random Username: {random_username}, Password: {random_password}"
        )

        # Tries to login with random credentials
        if account.login_to_account(random_username, random_password):
            break

        driver.refresh()

    specific_username = "test26sep"
    specific_password = "Test@123"
    print(f"\nNow testing with specific credentials...")
    account.login_to_account(specific_username, specific_password)

    driver.quit()  # Close the browser after login

# Run the login
if __name__ == "__main__":
    main()
