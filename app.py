from selenium import webdriver
import time

from pages.search_page import SearchPage

web_name = input('Please enter web address "http://www.otto.de": ')

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get(web_name)  # http://www.ottto.de
page = SearchPage(driver)

search_text = input('Please enter item to search: ')
page.text_input(search_text)

page.search_button()

time.sleep(7)
driver.close()
