from playwright.sync_api import Page


def test_can_load_homepage(page: Page):
    # 
    # Test to verify that the homepage loads correctly and contains expected content.
    # Args:
    #     page: Playwright Page object for browser interaction.
    # 
    page.goto("/")
    print(page.content())
    assert "Sign up" in page.content()