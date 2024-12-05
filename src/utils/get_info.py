import re


def check_page_version(page) -> str:
    new_table_div = page.locator('xpath=//*[@id="productDetails_expanderTables_depthLeftSections"]')
    is_new_table_div = new_table_div.count() > 0
    if is_new_table_div:
        return "new"
    else:
        return "old"


def get_product_review_stars(page):

    table_div = page.locator('//*[@id="productDetails-placement-auto_feature_div"]')
    try:
        customer_review_text_span = table_div.locator('//*[@id="acrCustomerReviewText"]')
        customer_review_text = customer_review_text_span.text_content(timeout=1000)
    except Exception as ex:
        customer_review_text = ""

    # //*[@id="acrPopover"]/span[1]/a/span
    try:
        stars_span = table_div.locator('//*[@id="acrPopover"]/span[1]/a/span')
        stars = stars_span.text_content(timeout=1000).strip()
    except Exception as ex:
        stars = ""

    return customer_review_text, stars


def get_rank_old_version(page):
    data = page.locator('xpath=//*[@id="productDetails_detailBullets_sections1"]').text_content(timeout=1000)
    data = data.split("Best Sellers Rank")[1]

    matches = re.findall(r'#\d{1,3}(?:,\d{3})*', data)

    return matches[0], matches[1]

def get_rank_new_version_base(page, xpath):
    table_div = page.locator(xpath)
    table_locator = table_div.locator('.a-keyvalue.prodDetTable').all_text_contents()

    for _ in table_locator:
        if "Best Sellers Rank" in _:
            table_locator_content = _.split("Best Sellers Rank")[1]
            matches = re.findall(r'#\d{1,3}(?:,\d{3})*', table_locator_content)
            return matches[0], matches[1]
    return "", ""

def get_rank_new_version(page):
    l1, l2 = get_rank_new_version_base(page, '//*[@id="productDetails_expanderTables_depthLeftSections"]')
    r1, r2 = get_rank_new_version_base(page, '//*[@id="productDetails_expanderTables_depthRightSections"]')

    if l1 != "":
        return l1, l2
    else:
        return r1, r2


def get_ranks(page):
    flag = ""
    try:
        html_version = check_page_version(page)
        if html_version == "new":
            rank1, rank2 = get_rank_new_version(page)
            flag = "new"
        else:
            rank1, rank2 = get_rank_old_version(page)
            flag = "old"
    except Exception as ex:
        rank1, rank2 = "", ""

    return rank1, rank2, flag



def get_ships_from(page):
    # //*[@id="fulfillerInfoFeature_feature_div"]/div[2]/div/span
    # //*[@id="fulfillerInfoFeature_feature_div"]/div[2]/div/span
    try:
        ships = page.locator('//*[@id="fulfillerInfoFeature_feature_div"]/div[2]/div/span')
        ships_data = ships.text_content(timeout=1000)

        if ships_data:
            if ships_data.lower() == "amazon":
                return "FBA"
            else:
                return "FBM"

    except Exception as ex:
        ships_data = ""

    return ships_data
