from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome webdriver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://www.imdb.com/search/name/")

# Define a function to wait for an element to be clickable
def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

# Fill input boxes
name_input = wait_for_element(driver, (By.ID, "searchField"))
name_input.send_keys("Leonardo DiCaprio")

# Select options from dropdown menus
gender_dropdown = wait_for_element(driver, (By.ID, "searchCategory"))
gender_dropdown.click()
wait_for_element(driver, (By.XPATH, "//option[contains(text(),'Actors')]")).click()

# Click the search button
search_button = wait_for_element(driver, (By.XPATH, "//button[@id='navbar-submit-button']"))
search_button.click()

# Wait for the results to load
wait_for_element(driver, (By.CLASS_NAME, "lister-list"))

# Close the browser
driver.quit()