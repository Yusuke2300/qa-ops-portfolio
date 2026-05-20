import pytest
from playwright.sync_api import Page, expect
from login_page import LoginPage

# 【データ駆動】3人分の異なるIDとパスワードのリストを用意する
test_users = [
    ("admin", "password"),
    ("test_user_1", "123456"),
    ("test_user_2", "qwerty")
]

# @pytest.mark.parametrize を使うと、リストのデータを順番にテストに流し込んでくれる
@pytest.mark.parametrize("username, password", test_users)
def test_login_success(page: Page, username: str, password: str):
    # 【手順の開始】ここは1回だけ書けばいい
    login_page = LoginPage(page)
    login_page.navigate()
    
    # 流し込まれた変数（username, password）を使ってログインする
    login_page.login(username, password)
    
    # ログアウトボタンが表示されることを確認
    expect(page.get_by_role("link", name="Logout")).to_be_visible()