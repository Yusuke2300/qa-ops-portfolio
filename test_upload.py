from playwright.sync_api import Page, expect

def test_file_upload(page: Page):
    # 1. 標的サイト（ファイルアップロードのテストページ）へ移動
    page.goto("https://the-internet.herokuapp.com/upload")
    
    # 2. ファイルをシステムに直接送り込む（★超重要）
    # "#file-upload" という見えない入力枠に対し、先ほど作ったダミーファイルをセットする
    page.locator("#file-upload").set_input_files("dummy.txt")
    
    # 3. アップロード実行ボタンをクリック
    page.locator("#file-submit").click()
    
    # 4. 検証（アサーション）：アップロード完了画面の確認
    # 画面に「File Uploaded!」という成功メッセージが出たか
    success_message = page.locator("h3")
    expect(success_message).to_have_text("File Uploaded!")
    
    # 送り込んだファイル名「dummy.txt」が画面に表示されているか
    uploaded_file_name = page.locator("#uploaded-files")
    expect(uploaded_file_name).to_contain_text("dummy.txt")