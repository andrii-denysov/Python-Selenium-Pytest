from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class StreamPage(BasePage):

    PLAY_PAUSE_BUTTON = (By.XPATH, "//*[contains(@class,'tw-transition')]/button")

    def wait_until_video_is_loaded(self):
        self.wait_for_element_to_be_present(self.PLAY_PAUSE_BUTTON)