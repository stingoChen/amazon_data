from dataclasses import dataclass


@dataclass
class ItemInfo:
    asin: str
    ships: str

    today_price: str
    typical_price: str
    discount_percentage: str

    brand_name: str

    coupon: str
    customer_review_text: str
    stars: str
    rank1: str
    rank2: str

    page_version: str
