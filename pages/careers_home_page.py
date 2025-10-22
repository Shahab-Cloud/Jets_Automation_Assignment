from playwright.sync_api import Page


class CareersHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://careers.justeattakeaway.com/global/en/home"
        self.search_box = page.get_by_placeholder("Search for job title")
        self.search_button = page.get_by_role("button", name="Search", exact=True)



    def open(self):
        self.page.goto(self.url)

    def search_job_title(self, title: str):
        self.search_box.fill(title)
        self.search_button.click()

    def select_category(self, category_name: str):
        self.search_box.click()
        self.page.locator(f'[data-ph-at-id="category-link"][data-ph-at-data-text="{category_name}"]').click()




