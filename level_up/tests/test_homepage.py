from playwright.sync_api import Page


def test_can_load_homepage(page: Page):
    page.goto("/")
    print(page.content())
    assert "Sign up" in page.content()