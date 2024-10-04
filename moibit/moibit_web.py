import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://moibit.io/") 
    driver.maximize_window()
    yield driver
    driver.quit()

def test_nav_links(driver):
    try:
        navbar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#navbarMenu"))
        )
        nav_links = navbar.find_elements(By.TAG_NAME, "a")

        for link in nav_links:
            link_name = link.text.strip()
            link_url = link.get_attribute("href")

            if not link_name or "mailto:" in link_url:
                print(f"Skipping link: {link_name or 'empty'}")
                continue

            print(f"Testing navbar link: {link_name} -> {link_url}")
            driver.get(link_url)
            time.sleep(2)

            # Check if the link redirected correctly
            if driver.current_url == link_url or link_url in driver.current_url:
                print(f"Navigation Link '{link_name}' is working and redirected successfully.")
            else:
                print(f"Navigation Link '{link_name}' did not redirect correctly or is broken.")

            driver.back()
            time.sleep(2)

    except TimeoutException:
        pytest.fail("Timeout: Navbar could not be located.")
    except Exception as e:
        pytest.fail(f"Error locating footer links: {e}")

def test_links(driver):
    try:
        # Adjust this selector to target the specific links you want to test
        link_elements = driver.find_elements(By.CSS_SELECTOR, ".link-class")  # Update with the correct selector

        for link in link_elements:
            link_name = link.find_element(By.TAG_NAME, "h4").text.strip()  # Assuming each link has an h4 element
            link_url = link.get_attribute("href")

            if not link_name or "mailto:" in link_url or link_url is None:
                print(f"Skipping link: {link_name or 'empty'}")
                continue

            print(f"Testing link: {link_name} -> {link_url}")

            driver.get(link_url)
            time.sleep(2)

            if driver.current_url == link_url or link_url in driver.current_url:
                print(f"Link '{link_name}' is working and redirected successfully.")
            else:
                print(f"Link '{link_name}' did not redirect correctly or is broken.")

            driver.back()
            time.sleep(2)

    except Exception as e:
        pytest.fail(f"Error locating link: {e}")
