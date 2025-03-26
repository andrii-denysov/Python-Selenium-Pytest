import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def initialize_driver(request):
    # Also exists a shorter option with only device name specification, so it can be used, depending on needs
    # mobile_emulation = {"deviceName": "Nexus 5"}
    mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
        "clientHints": {"platform": "Android", "mobile": True}}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://m.twitch.tv/")
    request.cls.driver = driver

    yield
    driver.quit()
