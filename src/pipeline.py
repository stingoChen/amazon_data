import time

from playwright.sync_api import sync_playwright
from tqdm import tqdm
from utils.get_brand import get_brand_name
from utils.get_info import get_product_review_stars, get_ranks, get_ships_from
from utils.price2pay import get_coupon, get_price_today
from configs import ItemInfo

import pandas as pd


def scrape_website(url, context):
    asin = url.split("/")[-1]
    page = context.new_page()
    page.goto(url)
    # page.screenshot(path="1.png", full_page=True)

    # with open("1.html", "w", encoding="utf-8") as file:
    #     file.write(page.content())

    try:
        ships = get_ships_from(page)
        brand_name = get_brand_name(page)
        today_price, typical_price, discount_percentage = get_price_today(page)
        coupon = get_coupon(page)
        customer_review_text, stars = get_product_review_stars(page)
        rank1, rank2, page_version = get_ranks(page)

        return ItemInfo(asin=asin, ships=ships, brand_name=brand_name, today_price=today_price, typical_price=typical_price, discount_percentage=discount_percentage, coupon=coupon, customer_review_text=customer_review_text, stars=stars, rank1=rank1, rank2=rank2, page_version=page_version)

    except Exception as e:
        print(e)


if __name__ == '__main__':

    with open("/Users/zcy/git/amazon_data/src/test1.txt", "r") as f:
        datas = f.readlines()
        datas = [_.strip() for _ in datas]

    df = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        browser_context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.37",
            locale = "en-US",
            timezone_id = "America/New_York"
        )
        for idx, _ in tqdm(enumerate(datas), total=len(datas)):
            r = scrape_website(_, browser_context)

            if idx == 0:
                df = {k: [v] for k, v in r.__dict__.items()}
            else:
                for k, v in r.__dict__.items():
                    df[k].append(v)
            # break
        browser.close()

    df = pd.DataFrame(df)

    df.to_excel("2024-12-25.xlsx", index=False)
