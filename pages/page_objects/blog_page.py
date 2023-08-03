from playwright.sync_api import Locator, Page

from pages.elements import TextInput
from pages.locators.blog_page_locators import BlogPageLocators
from pages.page_objects.base_page import BasePage


class BlogPage(BasePage):
    URL = "/blog"
    search_input = TextInput(BlogPageLocators.SEARCH_INPUT)

    def __init__(self, page: Page) -> None:
        super(BlogPage, self).__init__(page)
        self.search_submit = page.locator(BlogPageLocators.SEARCH_SUBMIT)
        self.get_searched_posts = page.locator(BlogPageLocators.POSTS)
        self.main_popup = page.locator(BlogPageLocators.MAIN_POPUP)

    def search_articles(self, search_query: str) -> None:
        self.search_input = search_query
        self.search_submit.click()

    def get_searched_link(self, link_text: str) -> Locator:
        return self.page.get_by_role("link", name=link_text)
