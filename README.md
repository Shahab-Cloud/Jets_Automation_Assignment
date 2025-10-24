# Just Eat Takeaway UI Automation (Playwright + JavaScript)
## Overview
Automated UI tests for the Just Eat Takeaway career portal using Playwright with JavaScript. Implements Page Object Model (POM) for cleaner, reusable test design.

## Project Structure
``` bash
jet-automation-task-js/
│
├── pages/
│   ├── careersHomePage.js       # Page Object Model for careers page
│   └── searchResultsPage.js        # Page Object Model for search results page
│
├── tests/
│   ├── test-search-test-jobs.spec.js    # Test Case 1: Job search using keyword "Test"
│   └── test-sales-jobs.spec.js      # Test Case 2: Job search using category "Sales"
│
├── utils/
│   └── pageHelper.js               # Helper methods for page interactions
│
├── playwright.config.js            # Playwright configuration
├── package.json                    # Project dependencies
├── package-lock.json               # Auto-generated lock file
└── README.md                       # Setup and execution instructions
```
## Prerequisites
Before running the tests, make sure you have:

- Node.js 16+ - Download and added to the environment path variables

- Google Chrome / Microsoft Edge / Firefox (for Playwright)

- Git

- Visual Studio Code (recommended IDE)

## Setup Instructions
1. Clone and Navigate to Project
```bash
git clone https://github.com/Shahab-Cloud/Jets_Automation_Assignment

cd jet-automation-task-js
```
2. Install Dependencies
```bash
npm install
```
3. Install Playwright Browsers
```bash
npx playwright install
```
## Design Pattern
The project follows the Page Object Model (POM) for maintainability and reusability.

Each page has its own class containing:

- Locators

- Page actions (like searching, filtering, validating results)

## Test Scenarios Automated
### Test Case 1: Job Search — Keyword "Test"
**Steps:**

1. Open the Careers Page

2. Enter job title "Test" and click Search

3. Verify search results appear from multiple locations

4. Refine search to Country: Netherlands

5. Verify that all results are now for Netherlands only

### Test Case 2: Job Search — Category "Sales"
**Steps:**

1. Open the Careers Page

2. Click on "Search for Job Title" and select "Sales" among Job Categories

3. Scroll to "Refine your search"

4. Verify Category "Sales" is selected and the search results number is matching

5. Refine search from the left panel to Country "Germany"

6. Verify the number of search results matches and category is "Sales" on all results

## Running the Tests
### Run All Tests
```bash
npx playwright test
```
### Run Specific Test File
```bash
npx playwright test tests/test-search-test-jobs.spec.js
npx playwright test tests/test-sales-jobs.spec.js
```
### Run in Headed Mode
```bash
npx playwright test --headed
```
### Run on Chrome Only
```bash
npx playwright test --project=chromium --headed
```
### Generate HTML Report
```bash
npx playwright test --reporter=html
npx playwright show-report
```
***Note:*** package-lock.json is automatically generated when you run npm install and should be committed to the repository to ensure consistent dependencies across installations.