# from playwright.sync_api import sync_playwright

def get_brand_name(page):
    # //*[@id="poExpander"]/div[1]/div/table/tbody/tr[6]/td[2]/span
    brand_name = page.locator("#productOverview_feature_div")
    brand_name = brand_name.all_text_contents()
    for _ in brand_name:
        if "Brand" in _:
            brand_name_str = _.split("Brand")[1].strip().split(" ")[0]
            return brand_name_str
    return ""
    #         print(brand_name_str)
    # # brand_name = brand_name.locator(".a-size-base.po-break-word").nth(0).first.text_content(timeout=1000).strip()
    # return brand_name


# if __name__ == "__main__":
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=True)
#         browser_context = browser.new_context(
#             user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
#         )
#
#         page = browser_context.new_page()
#         page.goto("https://www.amazon.com/dp/B09MBQN87R")
#         get_brand_name(page)
#

