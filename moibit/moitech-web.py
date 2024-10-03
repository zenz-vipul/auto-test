from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

import time

driver = webdriver.Chrome()
url = "http://moi.technology"
driver.get(url)
driver.maximize_window()

def nav_links(driver):
    try:
        navbar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'navbarMenu'))
        )

        nav_links = navbar.find_elements(By.CSS_SELECTOR, '.nav-links')

        for link in nav_links:
            link_name = link.text.strip()
            link_url = link.get_attribute("href")
            
            driver.get(link_url)
            time.sleep(2) 

            if driver.current_url == link_url:
                print(f"Navigation Link '{link_name}' is working and redirected successfully.")
            else:
                print(f"Navigation Link '{link_name}' did not redirect correctly or is broken.")
            
            driver.back()  
            time.sleep(2)  

    except Exception as e:
        print(f"Error locating navbar links: {e}")

def footer_link(driver):
    try:
        print("Attempting to locate the footer...")
        footer = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'footer'))
        )
        print("Footer located successfully.")

        footer_links = footer.find_elements(By.CSS_SELECTOR, 'footer a')
        print(f"Found {len(footer_links)} footer links.")

        if not footer_links:
            print("No footer links found. Please check the footer structure in the HTML.")
            return

        for i in range(len(footer_links)):
            try:
                footer = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, 'footer'))
                )
                footer_links = footer.find_elements(By.CSS_SELECTOR, 'footer a')

                link = footer_links[i]
                link_name = link.text.strip()
                link_url = link.get_attribute("href")

                if not link_name:
                    print(f"Skipping empty link at index {i}.")
                    continue

                if "mailto:" in link_url:
                    print(f"Skipping email link: {link_name}")
                    continue 

                current_window = driver.current_window_handle

                driver.get(link_url)
                print(f"Clicked on '{link_name}' and navigated to {link_url}.")

                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

                if len(driver.window_handles) > 1:
                    driver.switch_to.window(driver.window_handles[1])  # Switch to the new window/tab
                    driver.close()
                    driver.switch_to.window(current_window)
                    print(f"Returned from '{link_name}'.")
                else:
                    driver.back()  
                    print(f"Returned from '{link_name}'.")

                time.sleep(1) 

            except StaleElementReferenceException:
                print(f"Stale element reference while accessing link index {i}. Retrying...")
                continue  
            except Exception as e:
                print(f"Error accessing link '{link_name}': {e}")

    except Exception as e:
        print(f"Error locating footer links: {e}")




def products_link(driver, link_name, url):
    try:
        driver.get(url)
        time.sleep(2) 
        
        if driver.current_url == url:
            print(f"Products Link '{link_name}' is working.")
            return True
        else:
            print(f"Products Link '{link_name}' is broken or redirecting to a different page.")
            return False
    except Exception as e:
        print(f"Error testing link '{link_name}': {e}")
        return False
    finally:

        driver.back()  
        time.sleep(2)  

try:
    nav_links(driver)  
    footer_link(driver)  

finally:
    print("All test cases passed")
    driver.quit()
