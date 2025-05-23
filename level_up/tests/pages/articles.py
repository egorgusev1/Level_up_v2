from playwright.sync_api import Page


class ArticlesPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.start_new_article_button = page.get_by_role("link", name="Start new article")
        self.search_input = page.get_by_placeholder("Search articles")
        self.search_button = page.get_by_role("button", name="Search")
        self.clear_search_button = page.get_by_role("link", name="Clear search")

        #text elements
        self.welcome_heading = page.get_by_role("heading", name="Welcome")
        self.no_articles_message = page.get_by_text("You have no articles yet")
        