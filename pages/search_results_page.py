import re
import time

from playwright.sync_api import Page, expect

from utils.page_helper import PageHelper


class SearchResultsPage:
    def __init__(self, page: Page):
        self.helper = PageHelper(page)
        self.page = page
        self.result_cards = page.locator('[data-ph-at-id="jobs-list-item"]')
        self.location_labels = page.locator('[data-ph-at-id="job-location"]>div , [data-ph-at-id="job-info"] > span:nth-child(2)')
        self.category_labels = page.locator('[data-ph-at-id="job-category"]>div, [data-ph-at-id="job-info"] > span:nth-child(3)>span')
        self.country_button = page.get_by_role("button", name="Country")
        self.job_count_text = page.locator('[data-ph-at-id="search-page-top-job-count"]>span:nth-child(1)')

    def get_result_count(self):
        expect(self.result_cards.first).to_be_visible(timeout=5000)
        return self.result_cards.count()

    def get_all_locations(self):
        time.sleep(1)
        return [loc.text_content() for loc in self.location_labels.all()]

    def get_all_categories(self):
        time.sleep(2)
        return [cat.text_content() for cat in self.category_labels.all()]

    def refine_by_country(self, country_name: str):
        self.country_button.click()
        self.helper.scroll_to_text_in_container(
            "//legend[contains(text(), 'Country')]/following-sibling::ul",
            country_name
        )
        self.page.locator(f'[role="checkbox"][data-ph-at-text="{country_name}"]').check(force=True)

    def verify_selected_category(self, category_name: str):
        return self.page.locator(f'[role="checkbox"][data-ph-at-text="{category_name}"]').is_checked()

    def validate_jobs_count(self, category_name: str):
        job_count_text = self.job_count_text.text_content()
        category_job_count_text = self.page.locator(f'//*[@data-ph-at-text="{category_name}" and @ type="checkbox"]/following-sibling::span[@role="text"]/span/following-sibling::span').inner_text()
        category_job_count = re.search(r'\d+', category_job_count_text).group()
        assert job_count_text == category_job_count
