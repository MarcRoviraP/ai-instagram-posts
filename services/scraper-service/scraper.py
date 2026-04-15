from playwright.sync_api import sync_playwright

def fetch_html(url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )

        page = browser.new_page()
        page.goto(url, wait_until="networkidle")

        html = page.content()

        browser.close()
        return html