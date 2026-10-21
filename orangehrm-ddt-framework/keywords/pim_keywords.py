from pages.pim_page import PIMPage


class PIMKeywords:
    

    def __init__(self, page):
        self.page = page
        self.pim = PIMPage(page)

    def open_pim(self):
        """Tu khoa: Mo module PIM."""
        self.pim.open_pim_module()

    def add_employee(self, first_name, last_name):
        """Tu khoa: Them nhan vien moi thanh cong."""
        first_name = "" if (first_name is None or str(first_name) == "nan") else str(first_name)
        last_name = "" if (last_name is None or str(last_name) == "nan") else str(last_name)
        self.pim.open_add_employee_form()
        self.pim.fill_employee_name(first_name, last_name)
        self.pim.save_employee()

    def search_employee(self, name):
        """Tu khoa: Tim kiem nhan vien theo ten."""
        name = "" if (name is None or str(name) == "nan") else str(name)
        self.pim.open_employee_list()
        self.pim.search_by_name(name)

    def verify_search_result(self, expected_status):
        """Tu khoa: Xac minh ket qua tim kiem.
        expected_status: 'FOUND' hoac 'NOT_FOUND'.
        """
        count = self.pim.get_result_count()
        if expected_status == "FOUND":
            assert count >= 1, f"Khong tim thay nhan vien (so ket qua = {count})"
        elif expected_status == "NOT_FOUND":
            assert count == 0, f"Khong mong muon co ket qua nhung tim thay {count} ban ghi"
