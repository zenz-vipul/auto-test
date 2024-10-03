import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Avatar:
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

    # Test 3: Click on "Avatar" link
    def click_avatar_link(self):
        try:
            click_avatar_link = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[text()='Avatars']")
                )
            )
            click_avatar_link.click()
            print("Clicked 'Avatars' link.")
            time.sleep(5)  # Wait for 5 seconds
            try:
                avatars_text = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//article[text()='Your Avatars']")
                    )
                )
                print("Your Avatars text is present.")
            except TimeoutException:
                print("Your Avatars text is not present.")
        except TimeoutException:
            print("Timed out waiting for the 'Avatars' link to load.")
            print(self.driver.page_source)
        except Exception as e:
            print(f"An error occurred while clicking on avatar: {e}")
            
    def create_avatar_link(self):
        try:
            create_avatar_link = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[text()='Avatars']")
                )
            )
            create_avatar_link.click()
            print("Clicked 'Add New Avatar' link.")
            time.sleep(5)
        
def main():
    driver = webdriver.Chrome()
    avatar_test = Avatar(driver)
    avatar_test.setup("https://iome.ai")

    # Log in with specific credentials
    username = "VJ-108"
    password = "Test@123"
    avatar_test.login_to_account(username, password)
    avatar_test.click_avatar_link()

if __name__ == "__main__":
    main()
