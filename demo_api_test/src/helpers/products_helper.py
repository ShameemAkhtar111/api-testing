from demo_api_test.src.utilities.request_utilities import RequestUtilities


class ProductsHelper:

    def __init__(self):
        self.request_obj = RequestUtilities()

    def get_product_by_id(self, product_id):
        return self.request_obj.get(f"products/{product_id}")

    def call_create_product(self, payload):
        res = self.request_obj.post('products', payload=payload, expected_status_code=201)
        return res

    def call_list_products(self, payload=None):
        max_pages = 1000
        all_products = []

        for i in range(1, max_pages + 1):

            if not 'per_page' in payload.keys():
                payload['per_page'] = 100

            payload['page'] = i
            rs_api = self.request_obj.get('products', payload=payload)

            if not rs_api:
                break
            else:
                all_products.extend(rs_api)
        else:
            raise Exception(f"Unable to get all products after {max_pages} pages.")

        return all_products
