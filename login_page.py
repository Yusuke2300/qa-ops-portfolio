# login_page.py
from playwright.sync_api import Page

class LoginPage:
    # 1. 初期化：このページで使う「要素（部品）」を定義する
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.get_by_role("button", name="Login")

    # 2. アクション：ログイン画面へ移動する処理
    def navigate(self):
        self.page.goto("http://quotes.toscrape.com/login")

    # 3. アクション：ログインを実行する処理
    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()