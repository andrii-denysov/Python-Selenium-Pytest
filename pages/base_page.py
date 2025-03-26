from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    SEARCH_BUTTON = (By.XPATH, "//*[@href='/directory' and contains(@class, 'iEupwg')]")

    def __init__(self, driver):
        self.driver = driver
        self.webdriver_wait = WebDriverWait(self.driver, 5)

    def click_search_button_on_footer(self):
        self.wait_for_element_to_be_present(self.SEARCH_BUTTON)
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def scroll_a_bit(self):
        self.driver.execute_script("window.scrollBy(0, 250);")

    def perform_js_click(self, web_element):
        self.driver.execute_script("arguments[0].click();", web_element)

    def wait_for_element_to_be_present(self, locator):
        self.webdriver_wait.until(EC.presence_of_element_located(locator))

    def is_element_exist(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True
