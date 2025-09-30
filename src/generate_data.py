# from faker import Faker

import random
import string

class GenerateData:
    def __init__(self, coupon_length=15, prefix="AX"):
        self.coupon_length = coupon_length
        self.prefix = prefix
    
    def generate_coupon_codes(self):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=self.coupon_length))
        return code

    def generate_dataid(self ):
        customer = f"{self.prefix}{random.randint(100000, 200000)}"
        return customer
    
    
   