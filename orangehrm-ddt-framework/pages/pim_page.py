from pages.base_page import BasePage


class PIMPage(BasePage):
   

    MENU_PIM = 'span:has-text("PIM")'
    LINK_ADD_EMPLOYEE = 'a:has-text("Add Employee")'
    LINK_EMPLOYEE_LIST = 'a:has-text("Employee List")'
    INPUT_FIRST_NAME = 'input[name="firstName"]'
    INPUT_LAST_NAME = 'input[name="lastName"]'
    BTN_SAVE = 'button[type="submit"]'
    INPUT_SEARCH_NAME = 'input[placeholder="Type for hints..."]'
    BTN_SEARCH = 'button[type="submit"]'
    RESULT_ROWS = 'div.oxd-table-card'
    HEADER_PERSONAL_DETAILS = 'h6:has-text("Personal Details")'

    def open_pim_module(self):
        self.click_element(self.MENU_PIM)
        self.wait_for_heading("PIM")

    def open_add_employee_form(self):
        self.click_element(self.LINK_ADD_EMPLOYEE)
        self.page.wait_for_selector(self.INPUT_FIRST_NAME, timeout=10000)

    def fill_employee_name(self, first_name: str, last_name: str):
        self.fill_text(self.INPUT_FIRST_NAME, first_name)
        self.fill_text(self.INPUT_LAST_NAME, last_name)

    def save_employee(self):
        self.click_element(self.BTN_SAVE)
        self.wait_for_heading("Personal Details", timeout=15000)

    def open_employee_list(self):
        self.click_element(self.LINK_EMPLOYEE_LIST)
        self.page.wait_for_selector(self.INPUT_SEARCH_NAME, timeout=10000)

    def search_by_name(self, name: str):
        self.fill_text(self.INPUT_SEARCH_NAME, name)
        self.click_element(self.BTN_SEARCH)
        self.page.wait_for_timeout(1500)

    def get_result_count(self) -> int:
        return self.count_elements(self.RESULT_ROWS)
