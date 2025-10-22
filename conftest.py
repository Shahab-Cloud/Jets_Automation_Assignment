import pytest
from playwright.sync_api import sync_playwright
import json
import os

# Load Playwright config
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "playwright.config.json")
with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

# Get global use settings
global_use = config.get("use", {})
HEADLESS = global_use.get("headless", True)
VIEWPORT = global_use.get("viewport", {"width": 1280, "height": 800})

# Parameterize browsers from config projects
BROWSERS = [proj["use"]["browserName"] for proj in config.get("projects", [])]

@pytest.fixture(scope="function", params=BROWSERS)
def page(request):
    browser_name = request.param
    with sync_playwright() as p:
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=HEADLESS)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=HEADLESS)
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=HEADLESS)
        else:
            raise ValueError(f"Unknown browser: {browser_name}")

        context = browser.new_context(
            viewport=VIEWPORT
        )
        page = context.new_page()
        yield page
        context.close()
        browser.close()
