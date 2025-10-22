# Just Eat Takeaway UI Automation (Playwright + Python)

##  Overview
Automated UI tests for the Just Eat Takeaway career portal using **Playwright with Python**.
Implements Page Object Model (POM) for cleaner, reusable test design.

---

## Project Structure

```bash
Jet_Automation_Task/
│
├── pages/
│ ├── careers_home_page.py # Page Object Model (POM) for the careers page
│ └── search_results_page.py # Page Object Model (POM) for the search page
│
├── tests/
│ ├── test_search_test_jobs.py # Test Case 1: Job search using keyword "Test"
│ ├── test_sales_jobs.py # Test Case 2: Job search using category "Sales"
│
├── utils/
│ └──page_helper.py # contains helping methods
│
├── conftest.py # Fixture file for tests
├── README.md # Setup and execution instructions
├── playwright.config.json # playright configuration
└── requirements.txt # Python dependenciesfile
```

## Prerequisites

Before running the tests, make sure you have:

- **Python 3.9+** - The python path should be added to the environment variables
- **Google Chrome / Edge / Firefox** (for Playwright) - Update it in conftest.py to run on different browser
- **Git**

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shahab-Cloud/Jets_Automation_Assignment.git
   cd Jets_Automation_Assignment
   ```
   
2. **Create and Activate Virtual Environment**

Note: The .venv needs to be created first because it is related to the specific user for smooth run.

*On Windows (PowerShell)*
 ```bash
 python -m venv .venv

.venv\Scripts\activate
 ```


*On macOS / Linux*
 ```bash
 python3 -m venv .venv

source .venv/bin/activate
 ```


3️. Install Dependencies
 ```bash
 pip install -r requirements.txt
 ```


4️. Install Playwright Browsers
 ```bash
 playwright install
 ```


## Design Pattern

The project follows the Page Object Model (POM) for maintainability and reusability.

Each page (like the Careers page) has its own class containing:

- Locators

- Page actions (like searching, filtering, validating results)

## Test Scenarios Automated
- Test Case 1: Job Search — Keyword "Test"

Steps:

Open the Careers Page

Enter job title “Test” and click Search

Verify search results appear from multiple locations

Refine search to Country: Netherlands

Verify that all results are now for Netherlands only

- Test Case 2: Job Search — Category "Sales"

Steps:

Open the Careers Page

Click on “Search for Job Title” and select “Sales” among Job Categories

Scroll to “Refine your search”

Verify Category “Sales” is selected and the search results number is matching

Then Refine your search from the left panel to the Country “Germany”

Verify the number of the search results is matching and category is “Sales” on
all results

## Running the Tests
- Run All Tests 
 ```bash
 pytest -v
 ```


- Run a Specific Test File
 ```bash
pytest tests/test_search_test_jobs.py -v

pytest tests/test_sales_jobs.py -v

 ```

- Generate an HTML Report
 ```bash
 pytest --html=report.html --self-contained-html -v
 ```

## Author
Shahab Khan
Full Stack QA Engineer | Test Automation Specialist
[mohdshahabk17@gmail.com](mailto:mohdshahabk17@gmail.com)