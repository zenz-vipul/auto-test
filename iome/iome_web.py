import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    url = os.environ.get('URL') or 'https://iome.ai'   
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_nav_links(driver):
    try:
        navbar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.ant-col.flex.justify-end'))
        )
        nav_links = navbar.find_elements(By.TAG_NAME, 'a')

        for link in nav_links:
            link_name = link.text.strip()
            link_url = link.get_attribute("href")

            if not link_name or "mailto:" in link_url:
                print(f"Skipping link: {link_name or 'empty'}")
                continue
            
            print(f"Testing navbar link: {link_name} -> {link_url}")
            driver.get(link_url)
            
            time.sleep(3)
        
            expected_url = {
                "Digital You": "https://iome.ai/#the-digital-you",
                "Developer": "https://dev.iome.ai/",
                "Community": "https://iomeai.slack.com/join/shared_invite/zt-20s1w9jxg-unzBomKqMBrrq~DlYNpQHQ#/shared-invite/email",
                "Go to app": "https://iome.ai/login/"
            }
            
            assert driver.current_url == expected_url[link_name], f"Navigation Link '{link_name}' did not redirect correctly or is broken."
            
            driver.back()
            time.sleep(2)

    except TimeoutException:
        pytest.fail("Timeout: Navbar could not be located.")
    except Exception as e:
        pytest.fail(f"Error locating links: {e}") 

