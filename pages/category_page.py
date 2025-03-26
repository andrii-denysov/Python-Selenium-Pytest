from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CategoryPage(BasePage):
    STREAM_ITEMS = (By.XPATH, "//*[@role='list']/div//button[contains(@class,'tw-link')]")
    CLOSE_POPUP_BUTTON = (By.XPATH, "//*[@data-a-target='modalClose']")

    def select_stream(self):
        self.wait_for_element_to_be_present(self.STREAM_ITEMS)
        streams = self.driver.find_elements(*self.STREAM_ITEMS)
        for stream in streams:
            if stream.is_displayed():
                try:
                    self.perform_js_click(stream)
                except:
                    self.handle_popup()
                    self.perform_js_click(stream)

    def handle_popup(self):
        if self.is_element_exist(self.CLOSE_POPUP_BUTTON):
            self.driver.find_element(*self.CLOSE_POPUP_BUTTON).click()
