from playwright.sync_api import Page, expect


class BasePage:
    """Lop co so chung cho tat ca cac trang - chua cac hanh dong co ban."""

    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def click_element(self, selector: str):
        self.page.click(selector)

    def fill_text(self, selector: str, text: str):
        self.page.fill(selector, text)

    def verify_element_visible(self, selector: str):
        expect(self.page.locator(selector).first).to_be_visible()

    def verify_text_contains(self, selector: str, expected_text: str):
        actual = self.page.locator(selector).first.inner_text()
        assert expected_text in actual, f"Ky vao chua '{expected_text}', thuc te: '{actual}'"

    def wait_for_heading(self, heading_text: str, timeout: int = 15000):
        self.page.wait_for_selector(f'h6:has-text("{heading_text}")', timeout=timeout)

    def count_elements(self, selector: str) -> int:
        return self.page.locator(selector).count()
