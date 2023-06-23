from playwright.sync_api import Page

class LoginPage:
    URL = "https://github.com/login"

    def __init__(self, page:Page) -> None:
        self.page = page
        self.user_input = page.locator("//*[@id = 'login_field']")
        self.password_input = page.locator("//*[@id = 'password']")
        self.login_button = page.locator("//*[@value = 'Sign in']")
        self.forgot_pswd_button = page.locator("//*[(text()) = 'Forgot password?']")
    def navigate(self):
        self.page.goto(self.URL)

    def login_action(self, username: str, password: str):

        self.user_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()


