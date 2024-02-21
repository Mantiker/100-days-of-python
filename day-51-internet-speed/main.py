import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.speedtest.net/")

go_button = driver.find_element(By.CLASS_NAME, "js-start-test")
go_button.click()

test_completed = False

while not test_completed:
    time.sleep(1)
    check_elem = driver.find_element(By.CLASS_NAME, "upload-speed").text

    if len(check_elem) > 0 and check_elem != "—":
        test_completed = True


ping = driver.find_element(By.CLASS_NAME, "ping-speed").text
down_speed = driver.find_element(By.CLASS_NAME, "download-speed").text
up_speed = driver.find_element(By.CLASS_NAME, "upload-speed").text

print(f"Ping: {ping} ms")
print(f"Download speed: {down_speed} Mbps")
print(f"Upload speed: {up_speed} Mbps")
