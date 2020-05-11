from unittest import skip

from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class JobListingsTest(FunctionalTest):
    def test_landing_page(self):
        # Prospective Employee (PE) visits bbracesjobs website for
        # job opportunity
        self.browser.get(self.live_server_url)

        # They notices the page mentions Jobs and Careers
        self.assertIn("Jobs and Careers", self.browser.title)

        # Also there is a big text mentioning the company and site purpose
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("Business Brace Jobs and Careers", header_text)

        # a call-action-button was visible, asking to show opened
        # positions
        # Clicked on the CTA button as they see list of vacancy
        # Also noticing they are still on the same page.

        # TODO: uncomment and finish test
        # self.fail("Finish the test!")

    # def test_can_create_job_item(self):
    #     pass
