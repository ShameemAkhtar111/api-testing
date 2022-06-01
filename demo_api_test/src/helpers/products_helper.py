from demo_api_test.src.utilities.request_utilities import RequestUtilities


class ProductsHelper:

    def __init__(self):
        self.request_obj = RequestUtilities()

    def get_product_by_id(self, product_id):
        return self.request_obj.get(f"products/{product_id}")

    def call_create_product(self, payload):
        res = self.request_obj.post('products', payload=payload, expected_status_code=201)
        return res

    def call_list_products(self,payload=None):
        return self.request_obj.get('products', payload=payload)
