from playwright.sync_api import expect

class TimeEmployeePage:
    """Trang Employee Timesheets - bám sát giao diện thực tế OrangeHRM"""

    def __init__(self, page):
        self.page = page
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet"

        # === Form Select Employee ===
        self.form_title = 'h5:has-text("Select Employee"), div:has-text("Select Employee")'
        self.label_employee_name = 'label:has-text("Employee Name")'
        self.input_employee_name = 'input[placeholder="Type for hints..."]'
        self.text_required = 'span:has-text("Required"), *:has-text("Required")'
        self.btn_view_form = 'button.oxd-button--success:has-text("View")'
        self.autocomplete_option = 'div[role="option"], .oxd-autocomplete-option'

        # === Timesheets Pending Action ===
        self.section_pending = 'h5:has-text("Timesheets Pending Action"), div:has-text("Timesheets Pending Action")'
        self.text_records_found = ':has-text("Records Found")'
        self.pending_rows = '.orangehrm-container .oxd-table-card, .oxd-table-card'
        self.btn_view_row = 'button.oxd-button--ghost:has-text("View"), button:has-text("View")'

        # === Chi tiết Timesheet ===
        self.timesheet_detail_header = 'h6:has-text("Timesheet"), h5:has-text("Timesheet")'

    def open_page(self):
        """Mở trang Employee Timesheets"""
        self.page.goto(self.url)
        self.page.wait_for_timeout(2000)

    def verify_page_loaded(self):
        """Kiểm tra trang đã load - form Select Employee hiển thị"""
        expect(self.page.locator(self.input_employee_name)).to_be_visible(timeout=10000)

    def fill_employee_name(self, name):
        """Nhập tên nhân viên vào ô tìm kiếm"""
        if not name or name == "N_A":
            return
        self.page.fill(self.input_employee_name, "")
        self.page.fill(self.input_employee_name, name)
        self.page.wait_for_timeout(1500)  # Đợi gợi ý

    def select_autocomplete(self, name):
        """Chọn nhân viên từ danh sách gợi ý"""
        option = self.page.locator(f'{self.autocomplete_option}:has-text("{name}")')
        if option.count() > 0:
            option.first.click()
            self.page.wait_for_timeout(500)
            return True
        return False

    def click_view_form(self):
        """Nhấn nút View của form (xanh lá)"""
        self.page.click(self.btn_view_form)
        self.page.wait_for_timeout(2000)

    def click_view_first_row(self):
        """Nhấn nút View trên dòng đầu tiên của danh sách Pending"""
        btns = self.page.locator(self.btn_view_row)
        if btns.count() > 0:
            btns.first.click()
            self.page.wait_for_timeout(2000)

    def get_pending_records_count(self):
        """Đếm số dòng trong danh sách Pending"""
        return self.page.locator(self.pending_rows).count()

    def has_autocomplete_suggestion(self):
        """Kiểm tra có gợi ý nào hiển thị không"""
        return self.page.locator(self.autocomplete_option).count() > 0

    def verify_required_error(self):
        """Kiểm tra báo lỗi Required khi bỏ trống"""
        expect(self.page.locator(self.text_required).first).to_be_visible(timeout=5000)

    def verify_timesheet_detail_opened(self):
        """Kiểm tra trang chi tiết timesheet đã mở"""
        expect(self.page.locator(self.timesheet_detail_header).first).to_be_visible(timeout=10000)