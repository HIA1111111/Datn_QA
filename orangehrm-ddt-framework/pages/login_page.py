from pages.base_page import BasePage
from config.settings import BASE_URL


class LoginPage(BasePage):
    

    INPUT_USERNAME = 'input[name="username"]'
    INPUT_PASSWORD = 'input[name="password"]'
    BTN_LOGIN = 'button[type="submit"]'
    HEADER_DASHBOARD = 'h6:has-text("Dashboard")'
    MSG_INVALID = 'p.oxd-text.oxd-text--p.oxd-alert-content-text'
    MSG_REQUIRED = 'span.oxd-input-field-error-message'

    def open(self):
        self.goto(f"{BASE_URL}/auth/login")

    def enter_username(self, username: str):
        self.fill_text(self.INPUT_USERNAME, username)

    def enter_password(self, password: str):
        self.fill_text(self.INPUT_PASSWORD, password)

    def submit_login(self):
        self.click_element(self.BTN_LOGIN)
