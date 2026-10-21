


## Cấu trúc thu muc
```
orangehrm-ddt-framework/
├── pytest.ini              # Cau hinh pytest 
├── conftest.py             # Fixture trinh duyet + doc du lieu CSV
├── requirements.txt        # Thu vien can cai
├── config/
│   └── settings.py         # URL, tai khoan, timeout
├── data/                   # DU LIEU kiem thu (CSV)
│   ├── test_data_login.csv
│   ├── test_data_pim.csv
│   └── test_data_leave.csv
├── pages/                  # Lop trang (Page Object) - chua locator + hanh dong co ban
│   ├── base_page.py
│   ├── login_page.py
│   └── pim_page.py
├── keywords/               # TU KHOA nghiep vu - ket hop nhieu hanh dong thanh 1 tu khoa
│   ├── login_keywords.py
│   ├── pim_keywords.py
│   └── leave_keywords.py
├── tests/                  
│   ├── test_login_ddt.py   # Chuc nang: Dang nhap
│   ├── test_pim_ddt.py     # Chuc nang: PIM (quan ly nhan vien)
│   └── test_leave_ddt.py   # Chuc nang: Nghi phep
└── reports/                # Noi xuat bao cao
```

## Cai dat
```bash
pip install -r requirements.txt
playwright install chromium
```

## Cach chay
```bash
# 1. Kiem tra thu thap test case 
pytest --collect-only

# 2. Chay toan bo
pytest



# 4. Chay loc theo test case ID (vd: TC01, PIM03)
pytest -v -k "TC01 or TC02"

# 5. Xuat bao cao HTML
pytest --html=reports/report.html --self-contained-html
```

## Cach them test case moi
Chi can them 1 DONG moi vao file CSV tuong ung trong thu muc `data/`,
pytest se tu dong tao them test case moi - KHONG can sua code.

## Quy tac dam bao chay duoc (khong loi 0 item)
- Tep kiem thu: `test_*.py`
- Lop kiem thu: bat dau bang `Test*`
- Ham kiem thu: bat dau bang `test_*`
- Co `__init__.py` trong moi thu muc
- `pytest.ini` co `pythonpath = .` 

