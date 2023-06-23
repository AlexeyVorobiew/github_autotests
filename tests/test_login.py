from playwright.sync_api import Playwright, sync_playwright, expect, Page
from pages.login_page import LoginPage
import os
import inspect

valid_user = "silox59677@camplvad.com"
valid_password = "qweR1234!1"
notvalid_username = "user"
notvalid_password = "notexistpassword"

def test_valid_creds(page: Page,login_page: LoginPage) -> None:
    try:
        login_page.navigate()
        login_page.login_action(valid_user, valid_password)
        expect(page.get_by_text("Hi, I’m @silox59677")).to_be_visible() #мы на странице юзера, логин успешен
    except Exception as e:
        page.screenshot(path=f"tests/screens/{os.path.basename(__file__)}{inspect.stack()[0][3]}screenshot.png",
                    full_page=True)
        assert False, f" Случилась ошибка. Смотри скрин и текст ошибки для дебага: {e}"


def test_notvalid_creds(page: Page,login_page: LoginPage) -> None:
    try:
        login_page.navigate()
        login_page.login_action(notvalid_username, notvalid_username)
        expect(page.get_by_text("Incorrect username or password.")).to_be_visible() #проверка того, что появилась надпись о некорректных кредах
    except Exception as e:
        page.screenshot(path=f"tests/screens/{os.path.basename(__file__)}{inspect.stack()[0][3]}screenshot.png",
                    full_page=True)
        assert False, f" Случилась ошибка. Смотри скрин и текст ошибки для дебага: {e}"

