from playwright.sync_api import Page, expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page: Page):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    title = chromium_page.get_by_test_id("courses-list-toolbar-title-text")
    expect(title).to_have_text("Courses")

    icon = chromium_page.get_by_test_id("courses-list-empty-view-icon")
    expect(icon).to_have_class("MuiSvgIcon-root MuiSvgIcon-fontSizeLarge css-il79at")

    block_title = chromium_page.get_by_test_id("courses-list-empty-view-title-text")
    expect(block_title).to_have_text("There is no results")

    block_text = chromium_page.get_by_test_id("courses-list-empty-view-description-text")
    expect(block_text).to_have_text("Results from the load test pipeline will be displayed here")
