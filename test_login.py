from playwright.sync_api import Page, expect

# 関数名を「test_」から始めるのがPytestの絶対ルール
# 引数に「page」と入れるだけで、裏で勝手にブラウザを立ち上げて渡してくれる
def test_login(page: Page):
    # 1. ターゲットサイトへ移動
    page.goto("http://quotes.toscrape.com/")
    
    # 2. ログイン画面への移動
    page.get_by_role("link", name="Login").click()
    
    # 3. 認証情報の入力と実行
    page.locator("#username").fill("admin")
    page.locator("#password").fill("password")
    page.get_by_role("button", name="Login").click()

    # 4. アサーション（検証処理）
    expect(page.get_by_role("link", name="Logout")).to_be_visible()