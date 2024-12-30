from datetime import datetime

import pandas as pd
from playwright.sync_api import sync_playwright
from src.pipeline import scrape_website
from tqdm import tqdm

if __name__ == '__main__':
    now = datetime.now().strftime('%Y-%m-%d')

    with open(f"{now}.txt", "r") as f:
        datas = f.readlines()
        datas = [_.strip() for _ in datas]

    df = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        browser_context = browser.new_context(
            storage_state="/Users/zcy/git/amazon_data/test/state.json",
            # user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            # locale = "en-US",
            # timezone_id = "America/New_York"
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

    df.to_excel(f"{now}.xlsx", index=False)
