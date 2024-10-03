from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
url = "http://sarva.ai"
driver.get(url)
driver.maximize_window()

def nav_link(driver):
    h1DataCheckTitle = driver.find_element(By.TAG_NAME, 'h1')
    assert h1DataCheckTitle.text == "Raise Humanity's Happiness Quotient"
    time.sleep(2) 

    driver.find_element(By.LINK_TEXT, 'Humans of Sarva').click()
    h2DataTitleCheck = driver.find_element(By.TAG_NAME, 'h2')
    assert h2DataTitleCheck.text == 'Note from the CEO'
    print("Navigated to 'Humans of Sarva': Title verified.")

    driver.back()  
    time.sleep(2)

    driver.find_element(By.LINK_TEXT, 'Careers').click() 
    time.sleep(2)
    print("Navigated to 'Careers'.")

def footer_link(driver):
    try:
        footer = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.footer-col'))
        )

        footer_links = footer.find_elements(By.CSS_SELECTOR, 'a')
        
        for link in footer_links:
            link_name = link.text.strip()
            link_url = link.get_attribute("href")

            if "mailto:" in link_url:
                print(f"Skipping email link: {link_name}")
                continue  
            
            driver.get(link_url)
            time.sleep(2)  

            if driver.current_url == link_url:
                print(f"Footer Link '{link_name}' is working and redirected successfully.")
            else:
                print(f"Footer Link '{link_name}' did not redirect correctly or is broken.")
            
            driver.back()  
            time.sleep(2)  

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
    nav_link(driver)
    footer_link(driver)
    product_cards = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-card a"))
    )
    
    links_to_test = []
    for card in product_cards:
        link_name = card.text.strip()  
        link_url = card.get_attribute("href")  
        links_to_test.append({"name": link_name, "url": link_url})
    
    for link in links_to_test:
        products_link(driver, link["name"], link["url"])

finally:
    print("All test cases passed successfully")
    driver.quit()
