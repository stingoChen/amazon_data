from playwright.sync_api import sync_playwright


if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            locale = "en-US",
            timezone_id = "America/New_York"
        )

        page = context.new_page()
        page.goto("https://www.amazon.com/")

        page.wait_for_timeout(5000)

        page.hover('//*[@id="nav-global-location-slot"]')
        page.click('//*[@id="nav-global-location-slot"]')

        # page.wait_for_selector('xpath=//*[@id="a-popover-2"]/div', timeout=5000)

        page.hover('xpath=//*[@id="GLUXZipUpdateInput"]')
        page.fill('xpath=//*[@id="GLUXZipUpdateInput"]', "41094")
        page.wait_for_timeout(1000)

        page.hover('//*[@id="GLUXZipInputSection"]/div[2]')
        page.click('//*[@id="GLUXZipInputSection"]/div[2]')
        page.wait_for_timeout(1000)

        page.hover('//*[@id="a-autoid-1"]')
        page.click('//*[@id="a-autoid-1"]')
        page.wait_for_timeout(5000)

        context.storage_state(path="state.json")
        browser.close()
