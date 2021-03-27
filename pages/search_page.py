import re

from locators.search_page_locator import SearchPageLocators


class SearchPage:
    def __init__(self, browser):
        self.browser = browser

    def text_input(self, search_name: str):
        textbox = self.browser.find_element_by_css_selector(SearchPageLocators.SEARCH_TEXTBOX)
        textbox.send_keys(search_name)

    def search_button(self):
        button = self.browser.find_element_by_css_selector(SearchPageLocators.SEARCH_BUTTON)
        button.click()

    def select_price(self, min_price, max_price):
        min_textbox = self.browser.find_element_by_css_selector()

    def select_item(self):
        pass

    def cart_item(self):
        pass
