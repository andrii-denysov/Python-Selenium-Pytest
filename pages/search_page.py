from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):

    SEARCH_INPUT = (By.XPATH, "//input[@type='search']")
    SEARCH_RESULT_CATEGORY_xpath = "//a[contains(@href, 'category')]//p[@title='{}']"

    def perform_search_by_name(self, name):
        self.click_search_button_on_footer()
        self.wait_for_element_to_be_present(self.SEARCH_INPUT)
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(name)
        self.wait_for_element_to_be_present((By.XPATH, self.SEARCH_RESULT_CATEGORY_xpath.format(name)))
        self.driver.find_element(By.XPATH, self.SEARCH_RESULT_CATEGORY_xpath.format(name)).click()
