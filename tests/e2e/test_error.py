"""End-to-end tests for the error page"""

import re

from playwright.sync_api import Page, expect


def test_title(page: Page):
    """Tests error page title"""
    page.goto("/page/doesnt-exist")
    expect(page).to_have_title(re.compile("Something went wrong - FAT template"))


def test_text(page: Page):
    """Tests error page text"""
    page.goto("/page/doesnt-exist")
    expect(page.get_by_role("heading", name="Not Found")).to_be_visible()
    expect(page.get_by_test_id("status-code")).to_have_text("404")
