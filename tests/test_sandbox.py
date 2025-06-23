import pytest
from pages.sandbox_page import SandboxPage


def test_click_send(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.click_send()
