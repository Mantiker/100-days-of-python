import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def send_data(url: str, data):
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    time.sleep(2) # wait for loading

    fields = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    if len(fields) == 3:
        fields[0].send_keys(data["address"])
        fields[1].send_keys(data["price"])
        fields[2].send_keys(data["url"])

    time.sleep(1)

    # form = driver.find_element(By.CSS_SELECTOR, 'form[target="_self"]')
    form_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    form_button.click()

    time.sleep(1)
