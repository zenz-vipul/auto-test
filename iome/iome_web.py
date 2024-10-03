from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time

driver = webdriver.Chrome()
url = "https://iome.ai/"
driver.get(url)
driver.maximize_window()

# Navbar link tests
def nav_links(driver):
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
        
            if link_url.split("?")[0] in driver.current_url:
                print(f"Navigation Link '{link_name}' is working and redirected successfully.")
            else:
                print(f"Navigation Link '{link_name}' did not redirect correctly or is broken.")
            
            driver.back()
            time.sleep(2)

    except TimeoutException:
        print("Timeout: Navbar could not be located.")
    except Exception as e:
        print(f"Error locating links: {e}")

try:
    nav_links(driver)

finally:
    print("All test cases completed.")
    driver.quit()
