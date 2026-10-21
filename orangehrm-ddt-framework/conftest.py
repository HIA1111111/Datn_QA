import pytest
import pandas as pd
from pathlib import Path
from playwright.sync_api import sync_playwright, Page
from config.settings import (
    BASE_URL, VALID_USER, VALID_PASS, TIMEOUT, HEADLESS, SLOW_MO, DATA_FOLDER
)


def load_csv_data(filename: str):
    """Doc du lieu kiem thu tu file CSV, tu xu ly encoding, loi thi tra ve list rong."""
    path = Path(DATA_FOLDER) / filename
    try:
        df = pd.read_csv(path, encoding="utf-8-sig", keep_default_na=False).fillna("")
    except Exception:
        return []
    return df.to_dict("records")


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser) -> Page:
    page = browser.new_page()
    page.set_default_timeout(TIMEOUT)
    yield page
    page.close()


@pytest.fixture(scope="function")
def logged_in_page(page: Page) -> Page:
    """Fixture: dang nhap san voi tai khoan Admin, tra ve trang da vao Dashboard."""
    page.goto(f"{BASE_URL}/auth/login")
    page.fill('input[name="username"]', VALID_USER)
    page.fill('input[name="password"]', VALID_PASS)
    page.click('button[type="submit"]')
    page.wait_for_selector('h6:has-text("Dashboard")', timeout=TIMEOUT)
    yield page