import re

def get_price_today(page) -> tuple:
    """获取 商品今日价格"""
    apex_desktop = page.locator("#corePriceDisplay_desktop_feature_div")
    try:
        x = apex_desktop.locator(".a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay")
        price_whole = x.locator(".a-price-whole").first.text_content().strip()
        price_fraction = x.locator(".a-price-fraction").first.text_content().strip()
        today_price = float(f"{price_whole}{price_fraction}")
    except Exception as e:
        today_price = 0

    try:
        y = apex_desktop.locator(".a-section.a-spacing-small.aok-align-center").nth(0)
        typical_price = y.locator(".a-offscreen").first.text_content(timeout=1000).strip()[1:]
    except Exception as e:
        typical_price = 0

    try:
        z = apex_desktop.locator(".a-size-large.a-color-price.savingPriceOverride.aok-align-center.reinventPriceSavingsPercentageMargin.savingsPercentage")
        discount_percentage = z.first.text_content(timeout=1000).strip()
    except Exception as e:
        discount_percentage = 0

    return today_price, typical_price, discount_percentage


def get_coupon(page):
    coupon_data = page.locator("#promoPriceBlockMessage_feature_div")
    try:
        coupon = coupon_data.locator('label[id*="couponTextpctch"]').first.text_content(timeout=1000).strip()
        pattern = r"apply\s(.*?)\scoupon"
        match = re.search(pattern, coupon, re.IGNORECASE)
        if match:
            result = match.group(1)
            return result
    except Exception as e:
        return None


