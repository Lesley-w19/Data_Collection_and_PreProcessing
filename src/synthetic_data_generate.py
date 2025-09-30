from faker import Faker
import random
import pandas as pd

class SyntheticSalesData:
    def __init__(self,region, country, count=500, categories=None):
        self.fake = Faker()
        self.categories = categories or [
            'Cosmetics', 'Vegetables', 'Baby Food', 'Cereal', 'Fruits',
            'Clothes', 'Snacks', 'Household', 'Office Supplies', 'Beverages',
            'Personal Care', 'Meat'
        ]
        self.region = region
        self.country = country
        self.count = count

    def generate_city_lookup(self):
        return {
            "Region": random.choice(self.region),
            "Country": random.choice(self.country),
            "City": self.fake.city(),
            "Postal Code": self.fake.postcode()
        }

    def generate_product(self):
        return random.choice(self.categories)

    def generate_coupon_description(self):
        discount = random.choice(["10%", "25%", "Buy 1 Get 1", "Free Shipping"])
        product = self.generate_product()
        return f"{discount} off on {product}! Limited time offer."

    def generate_full_records(self):
        return {
            "Coupon Description": self.generate_coupon_description(),
            "Product": self.generate_product(),
            **self.generate_city_lookup()
        }

    def generate_product_records(self):
        # Generate DataFrame of `self.count` rows
        records = [self.generate_full_records() for _ in range(self.count)]
        return pd.DataFrame(records)
