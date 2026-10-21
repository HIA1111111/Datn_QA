from pages.login_page import LoginPage


class LoginKeywords:
    

    def __init__(self, page):
        self.page = page
        self.login_page = LoginPage(page)

    def navigate_to_login(self):
        """Tu khoa: Truy cap trang Dang nhap."""
        self.login_page.open()

    def input_credentials(self, username, password):
        """Tu khoa: Nhap ten dang nhap va mat khau (xu ly gia tri rong)."""
        username = "" if (username is None or str(username) == "nan") else str(username)
        password = "" if (password is None or str(password) == "nan") else str(password)
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)

    def click_login(self):
        """Tu khoa: Nhan nut Dang nhap."""
        self.login_page.submit_login()

    def verify_login_success(self):
        """Tu khoa: Xac minh dang nhap thanh cong (vào Dashboard)."""
        self.login_page.verify_element_visible(LoginPage.HEADER_DASHBOARD)

    def verify_error_displayed(self, error_type):
        """Tu khoa: Xac minh thong bao loi hien thi.
        error_type: 'Required' (truong bo trong) hoac 'Invalid credentials' (sai thong tin).
        """
        if error_type and "Required" in str(error_type):
            self.login_page.verify_element_visible(LoginPage.MSG_REQUIRED)
        else:
            self.login_page.verify_element_visible(LoginPage.MSG_INVALID)
