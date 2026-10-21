import pytest
from keywords.login_keywords import LoginKeywords
from conftest import load_csv_data

# Doc du lieu tu CSV -> tu dong tao test case theo tung dong
LOGIN_DATA = load_csv_data("test_data_login.csv")


class TestLoginDDT:
    

    @pytest.mark.parametrize("case", LOGIN_DATA, ids=[c["tc_id"] for c in LOGIN_DATA])
    def test_login_by_data(self, page, case):
        """Thuc hien kiem thu dang nhap theo tung dong du lieu trong CSV."""
        kw = LoginKeywords(page)
        kw.navigate_to_login()
        kw.input_credentials(case["username"], case["password"])
        kw.click_login()

        if case["expected_result"] == "SUCCESS":
            kw.verify_login_success()
        else:
            kw.verify_error_displayed(case["expected_message"])
