from playwright.sync_api import Page, expect

def test_dynamic_loading(page: Page):
    # 1. 標的サイトへ移動
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    
    # 2. Startボタンをクリック（裏側で数秒のローディングが開始される）
    page.locator("#start button").click()
    
    # 3. 検証（アサーション） 兼 動的待機
    hello_text = page.locator("#finish h4")
    
    # ★最重要ポイント：デフォルトのタイムアウト（5秒）を10秒に延長して待つ
    expect(hello_text).to_be_visible(timeout=10000)
    
    # 文字列が正しいことも確認
    expect(hello_text).to_have_text("Hello World!")