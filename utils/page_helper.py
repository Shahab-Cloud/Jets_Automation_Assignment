# utils/helper.py
from playwright.sync_api import Page

class PageHelper:
    def __init__(self, page: Page):
        self.page = page

    def scroll_to_text_in_container(self, container_selector: str, text: str):
        self.page.locator(
            f"{container_selector} >> text={text}"
        ).evaluate("el => el.scrollIntoView({block: 'center', behavior: 'instant'})")
