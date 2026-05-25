from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    # 1. 準備
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # 2. 実行
    page.goto("https://www.google.com/")
    
    # ロボットに文字を入力させる
    page.get_by_role("combobox", name="検索").fill("Playwright")
    
    # ロボットに「Enterキー」を押させる（検索の実行）
    page.keyboard.press("Enter")

    # 人間が結果を目視確認できるよう、3秒間だけ待機させる（Opsのデバッグテクニック）
    page.wait_for_timeout(3000)

    # 3. 終了
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)