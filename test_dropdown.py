from playwright.sync_api import Page, expect

def test_dropdown_selection(page: Page):
    # 1. 標的サイト（ドロップダウンのテストページ）へ移動
    page.goto("https://the-internet.herokuapp.com/dropdown")
    
    # 2. ドロップダウン要素を特定
    dropdown = page.locator("#dropdown")
    
    # 3. 操作：「Option 2」を選択する
    # select_option() は、ドロップダウン専用の強力なメソッド
    dropdown.select_option("Option 2")
    
    # 4. 検証（アサーション）：本当に「Option 2」が選ばれた状態になっているか確認
    # ドロップダウンの中で「現在選択されている要素（:checked）」のテキストを確認する
    selected_option = page.locator("#dropdown option:checked")
    expect(selected_option).to_have_text("Option 2")