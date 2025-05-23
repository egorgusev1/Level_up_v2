from playwright.sync_api import Page

from tests.pages.articles import ArticlesPage

def test_empty_articles_page(auth_page: Page):
    auth_page.goto("/articles/")
    articles_page = ArticlesPage(auth_page)
    assert articles_page.no_articles_message.is_visible()