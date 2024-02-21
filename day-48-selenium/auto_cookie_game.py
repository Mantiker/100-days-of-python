from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://orteil.dashnet.org/cookieclicker"

chrome_oprions = webdriver.ChromeOptions()
chrome_oprions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_oprions)
driver.get(URL)

time.sleep(5)

lang = driver.find_element(By.ID, "langSelect-EN")
if len(lang.text) > 0:
    lang.click()

time.sleep(2)

cookie = driver.find_element(By.ID, "bigCookie")

step = 3
next_check = time.time() + step
time_of_game_over = time.time() + 180

while time.time() < time_of_game_over:
    cookie.click()

    if time.time() > next_check:
        # check the upgrades
        upgrades = driver.find_elements(By.CSS_SELECTOR, "#upgrades .crate.enabled")
        for item in upgrades:
            item.click()

        # check the updates
        updates = driver.find_elements(By.CSS_SELECTOR, ".product.enabled")
        updates = updates[::-1]
        for item in updates:
            item.click()

        step += 0.1
        next_check = time.time() + step





