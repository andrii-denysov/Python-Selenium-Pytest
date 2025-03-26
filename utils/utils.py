import os
import sys
from datetime import datetime


class Utils:

    @staticmethod
    def get_root_directory():
        return sys.path[0]

    @staticmethod
    def save_screenshot_as_file(driver, test_name):
        current_date = "_" + datetime.now().strftime("%Y_%m_%d_%H-%M")
        save_path = os.path.join(Utils.get_root_directory(), "screenshots")
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        driver.save_screenshot(os.path.join(save_path, test_name + current_date + ".png"))