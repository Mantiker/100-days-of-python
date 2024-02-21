from selenium import webdriver
from selenium.webdriver.common.by import By

# Keeps chrome browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://hard.rozetka.com.ua/ua/airon_4822352781027/p213707179/")

price = driver.find_element(By.CLASS_NAME, value="product-price__big").text
if len(price) > 0:
    price = price[:-1]
print(price)

# driver.close()  # close 1 tab
driver.quit()  # quit the entire browser
