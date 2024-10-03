from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
url = "https://docs.moibit.io/"
driver.get(url)
driver.maximize_window()

try:
    # Wait for the sidebar to load
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "docSidebarContainer_0YBq"))
    )

    # Click the "Open menu" button to show the menu
    menu_button = driver.find_element(By.CLASS_NAME, "menu__button")

    # Check if the element is visible, enabled, and clickable
    if menu_button.is_displayed() and menu_button.is_enabled():
        driver.execute_script("arguments[0].click();", menu_button)
    else:
        print("The element is not visible, enabled, or clickable.")

    # Wait for the menu items to be visible
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "menu__list"))
    )

    # Test 1:  clicking on the "Introduction" link
    introduction_link = driver.find_element(By.LINK_TEXT, "Introduction")
    introduction_link.click()
    time.sleep(2)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "Introduction" in driver.title
    print("Test passed: Navigated to the Introduction page.")

    # Test 2:  clicking on the "Quick Start" link
    introduction_link = driver.find_element(By.LINK_TEXT, "Quick start")
    introduction_link.click()
    time.sleep(2)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "Quick start" in driver.title
    print("Test passed: Navigated to the Quick start page.")

    driver.back()

    # Wait for the API Overview dropdown to be fully expanded
    api_overview_link = driver.find_element(
        By.XPATH,
        "//a[@class='menu__link menu__link--sublist' and text()='API Overview']",
    )
    driver.execute_script("arguments[0].click();", api_overview_link)
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".menu__list-item--collapsed .menu__list")
        )
    )

    # Test 3: clicking on the "Authenticate MOI Bit User" link
    authenticate_link = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Authenticate MOI Bit User"))
    )
    authenticate_link.click()
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "Authenticate MOI Bit User" in driver.title
    print("Test passed: Navigated to the Authenticate MOI Bit User page.")

    # Wait for the File and Directory dropdown to be fully expanded
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[@class='menu__link menu__link--sublist' and text()='File and Directory']",
            )
        )
    )
    file_directory_link = driver.find_element(
        By.XPATH,
        "//a[@class='menu__link menu__link--sublist' and text()='File and Directory']",
    )
    driver.execute_script("arguments[0].click();", file_directory_link)
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".menu__list-item--collapsed .menu__list")
        )
    )

    # Test 4: clicking on the "writefiles" link
    authenticate_link = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.LINK_TEXT, "writefiles"))
    )
    authenticate_link.click()
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "writefiles" in driver.title
    print("Test passed: Navigated to the writefiles page.")

    # Test 5: clicking on the "writetexttofile" link
    authenticate_link = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.LINK_TEXT, "writetexttofile"))
    )
    authenticate_link.click()
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "writetexttofile" in driver.title
    print("Test passed: Navigated to the writetexttofile page.")

    # Test 6: Clicking on the "listfiles" link
    listfiles_link = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.LINK_TEXT, "listfiles"))
    )
    listfiles_link.click()
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "listfiles" in driver.title
    print("Test passed: Navigated to the listfiles page.")

    # Test 7: Clicking on the "readfile" link
    readfile_link = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.LINK_TEXT, "readfile"))
    )
    readfile_link.click()
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "readfile" in driver.title
    print("Test passed: Navigated to the readfile page.")

    # Test 8: Clicking on the "remove" link
    remove_link = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.LINK_TEXT, "remove"))
    )
    remove_link.click()
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "remove" in driver.title
    print("Test passed: Navigated to the remove page.")

    # Test 9: Clicking on the "listdeletedfiles" link
    listdeletedfiles_link = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.LINK_TEXT, "listdeletedfiles"))
    )
    listdeletedfiles_link.click()
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "listdeletedfiles" in driver.title
    print("Test passed: Navigated to the listdeletedfiles page.")

    # Test 10: Clicking on the "listfilesperdirectory" link
    listfilesperdirectory_link = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.LINK_TEXT, "listfilesperdirectory"))
    )
    listfilesperdirectory_link.click()
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "listfilesperdirectory" in driver.title
    print("Test passed: Navigated to the listfilesperdirectory page.")

    # Test 11: Clicking on the "makedir" link
    makedir_link = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.LINK_TEXT, "makedir"))
    )
    makedir_link.click()
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "makedir" in driver.title
    print("Test passed: Navigated to the makedir page.")

    # Test 12: Clicking on the "filestatus" link
    filestatus_link = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.LINK_TEXT, "filestatus"))
    )
    filestatus_link.click()
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "filestatus" in driver.title
    print("Test passed: Navigated to the filestatus page.")

    # Test 13: Clicking on the "versions" link
    versions_link = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.LINK_TEXT, "versions"))
    )
    driver.execute_script(
        "arguments[0].scrollIntoView(true);", versions_link
    )  
    time.sleep(1)
    versions_link.click()

    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "versions" in driver.title
    print("Test passed: Navigated to the versions page.")

    # Test 14: Clicking on the "moibitworld" link
    moibitworld_link = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.LINK_TEXT, "moibitworld"))
    )
    moibitworld_link.click()
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "moibitworld" in driver.title
    print("Test passed: Navigated to the moibitworld page.")

    # Test 15: Clicking on the "Get App details" link
    getappdetails_link = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Get App details"))
    )
    getappdetails_link.click()
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "Get App details" in driver.title
    print("Test passed: Navigated to the Get App details page.")

    # Test 16: Clicking on the "Get Developer Details" link
    getdevdetails_link = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Get Developer Details"))
    )
    getdevdetails_link.click()
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "Get Developer Details" in driver.title
    print("Test passed: Navigated to the Get Developer Details.")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[@class='menu__link menu__link--sublist' and text()='Enduser']",
            )
        )
    )
    enduser_link = driver.find_element(
        By.XPATH,
        "//a[@class='menu__link menu__link--sublist' and text()='Enduser']",
    )
    enduser_link.click()
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".menu__list-item--collapsed .menu__list")
        )
    )
    # Test 17: Clicking on the "addusertoapp" link
    addusertoapp_link = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "addusertoapp"))
    )
    addusertoapp_link.click()
    time.sleep(5)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "addusertoapp" in driver.title
    print("Test passed: Navigated to the addusertoapp.")

    # Test 18: Clicking on the "enduserdetails" link
    enduserdetails_link = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "enduserdetails"))
    )
    enduserdetails_link.click()
    driver.execute_script(
        "arguments[0].scrollIntoView(true);", enduserdetails_link
    )  
    time.sleep(5)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "enduserdetails" in driver.title
    print("Test passed: Navigated to the enduserdetails.")

    # Test 19: Clicking on the "updateenduser" link
    updateenduser_link = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "updateenduser"))
    )
    updateenduser_link.click()
    time.sleep(5)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "updateenduser" in driver.title
    print("Test passed: Navigated to the updateenduser.")

    # Test 20: Clicking on the "removeuser" link
    removeuser_link = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "removeuser"))
    )
    removeuser_link.click()
    time.sleep(5)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "removeuser" in driver.title
    print("Test passed: Navigated to the removeuser.")
    
    # Wait for the Network dropdown to be fully expanded
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[@class='menu__link menu__link--sublist' and text()='Network']",
            )
        )
    )
    network_link = driver.find_element(
        By.XPATH,
        "//a[@class='menu__link menu__link--sublist' and text()='Network']",
    )
    network_link.click()
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".menu__list-item--collapsed .menu__list")
        )
    )

    # Test 21: Clicking on the "getnetworks" link
    getnetworks_link = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "getnetworks"))
    )
    getnetworks_link.click()
    driver.execute_script(
        "arguments[0].scrollIntoView(true);", getappdetails_link
    ) 
    time.sleep(5)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "getnetworks" in driver.title
    print("Test passed: Navigated to the getnetworks.")

    # Test 22: Clicking on the "getnetwork" link
    getnetwork_link = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "getnetwork"))
    )
    getnetwork_link.click()
    time.sleep(5)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "getnetwork" in driver.title
    print("Test passed: Navigated to the getnetwork.")
    
    # Test 23:  clicking on the "Storage Used" link
    storageused_link = driver.find_element(By.LINK_TEXT, "Storage Used")
    storageused_link.click()
    time.sleep(2)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "Storage Used" in driver.title
    print("Test passed: Navigated to the Storage Used.")

except Exception as e:
    print("An error occurred: ", str(e))

finally:
    driver.quit()
