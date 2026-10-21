import pytest
from keywords.leave_keywords import LeaveKeywords
from conftest import load_csv_data

LEAVE_DATA = load_csv_data("test_data_leave.csv")


class TestLeaveDDT:
    

    @pytest.mark.parametrize("case", LEAVE_DATA, ids=[c["tc_id"] for c in LEAVE_DATA])
    def test_leave_by_data(self, logged_in_page, case):
        """Kiem thu dieu huong module Nghi phep theo du lieu CSV."""
        kw = LeaveKeywords(logged_in_page)

        action = case["action"]
        if action == "Mo trang Nghi phep":
            kw.open_leave_module()
        elif action == "Mo form dang ky nghi":
            kw.open_leave_module()
            kw.open_apply_form()
            kw.verify_apply_form_visible()
