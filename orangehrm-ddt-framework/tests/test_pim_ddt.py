import pytest
from keywords.pim_keywords import PIMKeywords
from conftest import load_csv_data

PIM_DATA = load_csv_data("test_data_pim.csv")


class TestPIMDDT:
    

    @pytest.mark.parametrize("case", PIM_DATA, ids=[c["tc_id"] for c in PIM_DATA])
    def test_pim_by_data(self, logged_in_page, case):
        
        kw = PIMKeywords(logged_in_page)
        kw.open_pim()

        action = case["action"]
        if action == "Them nhan vien moi":
            kw.add_employee(case["first_name"], case["last_name"])
        elif action.startswith("Tim kiem"):
            kw.search_employee(case["first_name"])
            kw.verify_search_result(case["expected_status"])
