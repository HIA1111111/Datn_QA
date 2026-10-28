import pytest
from conftest import load_csv_data
from keywords.time_employee_keywords import TimeEmployeeKeywords

# === Đọc dữ liệu từ CSV ===
TIME_DATA = load_csv_data("time_employee_timesheet.csv")

# === DỰ PHÒNG: LUÔN CÓ 6 ITEM — KHÔNG BAO GIỜ 0 ===
if not TIME_DATA:
    print("⚠️ Dùng dữ liệu dự phòng cho Time Employee Timesheet")
    TIME_DATA = [
        {"tc_id": "TIME01", "action": "mo_trang_employee_timesheets", "employee_name": "N_A", "expected_result": "Form Select Employee hien thi"},
        {"tc_id": "TIME02", "action": "bo_trong_nhan_view", "employee_name": "", "expected_result": "Bao loi Required"},
        {"tc_id": "TIME03", "action": "tim_nhan_vien_ton_tai", "employee_name": "Raja Rames Mar", "expected_result": "Hien thi bang cham cong"},
        {"tc_id": "TIME04", "action": "kiem_tra_danh_sach_pending", "employee_name": "N_A", "expected_result": "Co records hien thi"},
        {"tc_id": "TIME05", "action": "tim_nhan_vien_khong_ton_tai", "employee_name": "NguoiKhongCoXYZ", "expected_result": "Khong co goi y"},
        {"tc_id": "TIME06", "action": "xem_chi_tiet_timesheet", "employee_name": "Raja Rames Mar", "expected_result": "Mo trang chi tiet timesheet"},
    ]

class TestTimeEmployeeDDT:
    """Bộ kiểm thử Employee Timesheets — DDT + Từ khóa, bám sát web thực tế"""

    @pytest.mark.parametrize("case", TIME_DATA, ids=[row["tc_id"] for row in TIME_DATA])
    def test_employee_timesheet(self, logged_in_page, case):
        # logged_in_page đã đăng nhập sẵn — không cần đăng nhập lại
        kw = TimeEmployeeKeywords(logged_in_page)

        action = case["action"]
        emp_name = "" if case["employee_name"] == "N_A" else case["employee_name"]

        # === Thực thi theo hành động ===
        if action == "mo_trang_employee_timesheets":
            kw.open_employee_timesheet_page()

        elif action == "bo_trong_nhan_view":
            kw.open_employee_timesheet_page()
            kw.search_with_empty_name()

        elif action == "tim_nhan_vien_ton_tai":
            kw.open_employee_timesheet_page()
            kw.search_existing_employee(emp_name)

        elif action == "kiem_tra_danh_sach_pending":
            kw.open_employee_timesheet_page()
            kw.check_pending_list()

        elif action == "tim_nhan_vien_khong_ton_tai":
            kw.open_employee_timesheet_page()
            kw.search_nonexistent_employee(emp_name)

        elif action == "xem_chi_tiet_timesheet":
            kw.open_employee_timesheet_page()
            kw.view_timesheet_detail(emp_name)