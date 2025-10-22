import pytest
from pages.careers_home_page import CareersHomePage
from pages.search_results_page import SearchResultsPage

@pytest.mark.ui
def test_sales_category_refine_germany(page):
    home = CareersHomePage(page)
    home.open()
    home.select_category("Sales")

    results = SearchResultsPage(page)
    count_before = results.get_result_count()
    assert count_before > 0, "No Sales jobs found initially"

    # Is category selected
    is_category_selected = results.verify_selected_category("Sales")
    assert is_category_selected is True, f"Expected category to be selected, but was {is_category_selected}"

    results.validate_jobs_count("Sales")
    categories = results.get_all_categories()
    for cat in categories:
        assert "Sales" in cat, f"Unexpected category found: {cat}"

    # Refine to Germany
    results.refine_by_country("Germany")
    count_after = results.get_result_count()
    assert count_after <= count_before, "Refined result count didn't reduce or stay same"

    # Verify all are Sales + Germany
    categories = results.get_all_categories()
    locations = results.get_all_locations()
    for cat in categories:
        assert "Sales" in cat, f"Non-Sales job found: {cat}"
    for loc in locations:
        assert "Germany" in loc, f"Job not in Germany: {loc}"
