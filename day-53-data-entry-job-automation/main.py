import os

import dotenv

import zillow
import google_form

dotenv.load_dotenv()

GOOGLE_FORM_URL = os.getenv("GOOGLE_FORM_URL")

zillow_url = "https://www.zillow.com/baltimore-md/rentals/?itc=renter_zw_zh_homepage-renter-rtb_btn_find-rentals&searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Afalse%2C%22mapBounds%22%3A%7B%22west%22%3A-76.89033768457031%2C%22east%22%3A-76.35063431542969%2C%22south%22%3A39.10389389084713%2C%22north%22%3A39.489672845582845%7D%2C%22mapZoom%22%3A11%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A3523%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3Anull%2C%22max%22%3A1600%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"

list = zillow.get_rent_list(zillow_url)

for v in list:
    google_form.send_data(GOOGLE_FORM_URL, v)
