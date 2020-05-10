
from .base import FunctionalTest


class JobListingsTest(FunctionalTest):

    def test_landing_page(self):
        self.browser.get(self.live_server_url)

        self.assertIn("Jobs and Careers", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("Business Brace Jobs and Careers", header_text)

    def test_can_create_job_item(self):
        pass
