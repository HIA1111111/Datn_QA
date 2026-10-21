from pages.base_page import BasePage


class LeaveKeywords:
    

    MENU_LEAVE = 'span:has-text("Leave")'
    LINK_APPLY = 'a:has-text("Apply")'
    LABEL_LEAVE_TYPE = 'label:has-text("Leave Type")'

    def __init__(self, page):
        self.page = page
        self.base = BasePage(page)

    def open_leave_module(self):
        """Tu khoa: Mo module Nghi phep."""
        self.base.click_element(self.MENU_LEAVE)
        self.base.wait_for_heading("Leave")

    def open_apply_form(self):
        """Tu khoa: Mo form dang ky nghi phep."""
        self.base.click_element(self.LINK_APPLY)
        self.page.wait_for_selector(self.LABEL_LEAVE_TYPE, timeout=10000)

    def verify_apply_form_visible(self):
        """Tu khoa: Xac minh form dang ky nghi hien thi day du."""
        self.base.verify_element_visible(self.LABEL_LEAVE_TYPE)
