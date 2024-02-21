from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keeps chrome browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count_element = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

article_count = ''.join(article_count_element.text.split(","))
print(article_count)
# article_count_element.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)

# driver.quit()  # quit the entire browser
