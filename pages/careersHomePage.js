const { expect } = require('@playwright/test');

class CareersHomePage {
    constructor(page) {
        this.page = page;
        this.url = "/global/en/home";
        this.searchBox = page.getByPlaceholder("Search for job title");
        this.searchButton = page.getByRole("button", { name: "Search", exact: true });
    }

    async open() {
        await this.page.goto(this.url);
    }

    async searchJobTitle(title) {
        await this.searchBox.fill(title);
        await this.searchButton.click();
    }

    async selectCategory(categoryName) {
        await this.searchBox.click();
        await this.page.locator(`[data-ph-at-id="category-link"][data-ph-at-data-text="${categoryName}"]`).click();
    }
}

module.exports = CareersHomePage;