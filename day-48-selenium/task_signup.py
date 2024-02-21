from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

first_name_element = driver.find_element(By.NAME, "fName")
last_name_element = driver.find_element(By.NAME, "lName")
email_element = driver.find_element(By.NAME, "email")

first_name_element.send_keys("James")
last_name_element.send_keys("Bond")
email_element.send_keys("bond@tttt.tt")

submit_button = driver.find_element(By.CSS_SELECTOR, ".form-signin button")
submit_button.send_keys(Keys.ENTER)

# submit_button.submit()
# submit_button.click()

# driver.quit()
