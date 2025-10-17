from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        for i in range(1, 11):
            page.goto(f"file:///app/layout-{i}.html")
            page.screenshot(path=f"jules-scratch/verification/layout-{i}.png")
        browser.close()

if __name__ == "__main__":
    run()
