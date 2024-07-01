"""End-to-end tests for homepage"""

import re

from playwright.sync_api import Page, expect


def test_title(page: Page):
    """Tests homepage title"""
    page.goto("/")
    expect(page).to_have_title(re.compile("FAT template"))


def test_text(page: Page):
    """Tests homepage text"""
    page.goto("/")
    expect(page.get_by_role("heading", name="Let's start coding 😊?")).to_be_visible()
    expect(
        page.get_by_test_id("no-text"), page.get_by_test_id("yes-text")
    ).to_be_hidden()


def test_click_yes_button(page: Page):
    """
    Tests that yes-text shows
    When clicking in 'Yes' button
    """
    page.goto("/")
    page.get_by_role("button", name="Yes").click()
    expect(page.get_by_test_id("yes-text")).to_be_visible()
    expect(page.get_by_test_id("no-text")).to_be_hidden()


def test_click_no_button(page: Page):
    """
    Tests that no-text shows
    When clicking in 'No' button
    """
    page.goto("/")
    page.get_by_role("button", name="No").click()
    expect(page.get_by_test_id("no-text")).to_be_visible()
    expect(page.get_by_test_id("yes-text")).to_be_hidden()
