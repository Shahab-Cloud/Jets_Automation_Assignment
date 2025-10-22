import pytest
from pages.careers_home_page import CareersHomePage
from pages.search_results_page import SearchResultsPage

@pytest.mark.ui
def test_search_test_jobs(page):
    home = CareersHomePage(page)
    home.open()
    home.search_job_title("Test")

    results = SearchResultsPage(page)
    assert results.get_result_count() > 0, "No jobs found for 'Test'"

    # Verify results come from multiple locations
    locations = results.get_all_locations()
    unique_locations = set(locations)
    assert len(unique_locations) > 1, f"Expected multiple locations, found {unique_locations}"

    # Refine by Netherlands
    results.refine_by_country("Netherlands")

    # Verify all jobs are in Netherlands
    locations = results.get_all_locations()
    for loc in locations:
        assert "Netherlands" in loc, f"Found job outside Netherlands: {loc}"
