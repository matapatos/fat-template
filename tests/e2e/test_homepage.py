"""End-to-end tests for homepage"""

import re

from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    """Tests homepage title"""
    page.goto("http://localhost:8000/")
    expect(page).to_have_title(re.compile("FAT boilerplate"))
