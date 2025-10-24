const { test, expect } = require('@playwright/test');
const CareersHomePage = require('../pages/careersHomePage');
const SearchResultsPage = require('../pages/searchResultsPage');

test('sales category refine germany', async ({ page }) => {
    const home = new CareersHomePage(page);
    await home.open();
    await home.selectCategory("Sales");

    const results = new SearchResultsPage(page);
    const countBefore = await results.getResultCount();
    expect(countBefore, "No Sales jobs found initially").toBeGreaterThan(0);

    // Is category selected
    const isCategorySelected = await results.verifySelectedCategory("Sales");
    expect(isCategorySelected, `Expected category to be selected, but was ${isCategorySelected}`).toBe(true);

    await results.validateJobsCount("Sales");
    const categories = await results.getAllCategories();
    
    for (const cat of categories) {
        expect(cat, `Unexpected category found: ${cat}`).toContain("Sales");
    }

    // Refine to Germany
    await results.refineByCountry("Germany");
    const countAfter = await results.getResultCount();
    expect(countAfter, `Refined result count didn't reduce or stay same`).toBeLessThanOrEqual(countBefore);

    // Verify all are Sales + Germany
    const categoriesAfter = await results.getAllCategories();
    const locations = await results.getAllLocations();
    
    for (const cat of categoriesAfter) {
        expect(cat, `Non-Sales job found: ${cat}`).toContain("Sales");
    }
    
    for (const loc of locations) {
        expect(loc, `Job not in Germany: ${loc}`).toContain("Germany");
    }
});