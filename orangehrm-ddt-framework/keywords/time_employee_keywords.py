from pages.time_employee_page import TimeEmployeePage

class TimeEmployeeKeywords:
    """Từ khóa nghiệp vụ trang Employee Timesheets"""

    def __init__(self, page):
        self.page = page
        self.time_page = TimeEmployeePage(page)

    def open_employee_timesheet_page(self):
        """Mở trang Employee Timesheets và kiểm tra load"""
        self.time_page.open_page()
        self.time_page.verify_page_loaded()

    def search_with_empty_name(self):
        """Bỏ trống tên → nhấn View → kiểm tra lỗi Required"""
        self.time_page.fill_employee_name("")
        self.time_page.click_view_form()
        self.time_page.verify_required_error()

    def search_existing_employee(self, emp_name):
        """Tìm nhân viên tồn tại → chọn gợi ý → nhấn View"""
        self.time_page.fill_employee_name(emp_name)
        found = self.time_page.select_autocomplete(emp_name)
        assert found, f"Không tìm thấy gợi ý cho: {emp_name}"
        self.time_page.click_view_form()

    def check_pending_list(self):
        """Kiểm tra danh sách Timesheets Pending Action có dữ liệu"""
        count = self.time_page.get_pending_records_count()
        assert count >= 1, f"Danh sách Pending trống, tìm thấy {count} dòng"

    def search_nonexistent_employee(self, emp_name):
        """Tìm nhân viên không tồn tại → không có gợi ý"""
        self.time_page.fill_employee_name(emp_name)
        has_suggestion = self.time_page.has_autocomplete_suggestion()
        assert not has_suggestion, "Vẫn hiện gợi ý dù tên không tồn tại"

    def view_timesheet_detail(self, emp_name):
        """Tìm nhân viên → nhấn View trên dòng đầu tiên → xem chi tiết"""
        self.time_page.fill_employee_name(emp_name)
        self.time_page.select_autocomplete(emp_name)
        self.time_page.click_view_form()
        self.time_page.click_view_first_row()
        self.time_page.verify_timesheet_detail_opened()