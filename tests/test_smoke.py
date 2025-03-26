import pytest

from pages.category_page import CategoryPage
from pages.search_page import SearchPage
from pages.stream_page import StreamPage
from tests.test_base import BaseTest
from utils.utils import Utils

@pytest.mark.smoke
class TestSmoke(BaseTest):
    STAR_CRAFT_II = "StarCraft II"

    def test_smoke_happy_path(self, request):
        search_page = SearchPage(self.driver)
        category_page = CategoryPage(self.driver)
        stream_page = StreamPage(self.driver)
        search_page.perform_search_by_name(self.STAR_CRAFT_II)
        category_page.scroll_a_bit()
        category_page.scroll_a_bit()
        category_page.select_stream()
        stream_page.wait_until_video_is_loaded()
        Utils.save_screenshot_as_file(self.driver, request.node.originalname)
