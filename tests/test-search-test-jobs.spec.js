const { test, expect } = require('@playwright/test');
const CareersHomePage = require('../pages/careersHomePage');
const SearchResultsPage = require('../pages/searchResultsPage');

test('search test jobs', async ({ page }) => {
    const home = new CareersHomePage(page);
    await home.open();
    await home.searchJobTitle("Test");

    const results = new SearchResultsPage(page);
    const resultCount = await results.getResultCount();
    expect(resultCount, "No jobs found for 'Test'").toBeGreaterThan(0);

    // Verify results come from multiple locations
    const locations = await results.getAllLocations();
    const uniqueLocations = [...new Set(locations)];
    expect(uniqueLocations.length, `Expected multiple locations, found ${uniqueLocations}`).toBeGreaterThan(1);

    // Refine by Netherlands
    await results.refineByCountry("Netherlands");

    // Verify all jobs are in Netherlands
    const locationsAfter = await results.getAllLocations();
    for (const loc of locationsAfter) {
        expect(loc, `Found job outside Netherlands: ${loc}`).toContain("Netherlands");
    }
});