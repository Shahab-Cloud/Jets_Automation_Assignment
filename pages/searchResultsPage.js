const { expect } = require('@playwright/test');
const PageHelper = require('../utils/pageHelper'); 

class SearchResultsPage {
    constructor(page) {
        this.helper = new PageHelper(page);
        this.page = page;
        this.resultCards = page.locator('[data-ph-at-id="jobs-list-item"]');
        this.locationLabels = page.locator('[data-ph-at-id="job-location"]>div , [data-ph-at-id="job-info"] > span:nth-child(2)');
        this.categoryLabels = page.locator('[data-ph-at-id="job-category"]>div, [data-ph-at-id="job-info"] > span:nth-child(3)>span');
        this.countryButton = page.getByRole("button", { name: "Country" });
        this.jobCountText = page.locator('[data-ph-at-id="search-page-top-job-count"]>span:nth-child(1)');
    }

    async getResultCount() {
        await expect(this.resultCards.first()).toBeVisible({ timeout: 5000 });
        return await this.resultCards.count();
    }

    async getAllLocations() {
        await this.page.waitForTimeout(1000);
        const locations = await this.locationLabels.all();
        return await Promise.all(locations.map(async loc => await loc.textContent()));
    }

    async getAllCategories() {
        await this.page.waitForTimeout(2000);
        const categories = await this.categoryLabels.all();
        return await Promise.all(categories.map(async cat => await cat.textContent()));
    }

    async refineByCountry(countryName) {
        await this.countryButton.click();
        await this.helper.scrollToTextInContainer(
            "//legend[contains(text(), 'Country')]/following-sibling::ul",
            countryName
        );
        await this.page.locator(`[role="checkbox"][data-ph-at-text="${countryName}"]`).check({ force: true });
    }

    async verifySelectedCategory(categoryName) {
        return await this.page.locator(`[role="checkbox"][data-ph-at-text="${categoryName}"]`).isChecked();
    }

    async validateJobsCount(categoryName) {
        const jobCountText = await this.jobCountText.textContent();
        const categoryJobCountText = await this.page.locator(`//*[@data-ph-at-text="${categoryName}" and @ type="checkbox"]/following-sibling::span[@role="text"]/span/following-sibling::span`).innerText();
        const categoryJobCount = categoryJobCountText.match(/\d+/)[0];
        
        expect(jobCountText).toBe(categoryJobCount);
    }
}

module.exports = SearchResultsPage;