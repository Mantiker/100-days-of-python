from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://python.org"

driver = webdriver.Chrome()
driver.get(URL)

elements = driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul.menu li")

events = {}
for idx, e in enumerate(elements):
    events[idx] = {
        "time": e.find_element(By.TAG_NAME, "time").text,
        "name": e.find_element(By.TAG_NAME, "a").text,
        "url": e.find_element(By.TAG_NAME, "a").get_attribute("href"),
    }

print(events)