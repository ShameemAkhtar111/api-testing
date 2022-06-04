import json
import os
from demo_api_test.src.utilities.wooComApiUtilities import WooComAPIUtilities


class OrdersHelper:

    def __init__(self):
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.wooApiObj = WooComAPIUtilities()

    def create_order(self, additional_args=None):
        payload_template = os.path.join(self.cur_file_dir, '..', 'data', 'create_order_payload.json')
        with open(payload_template) as file:
            payload = json.load(file)

        if additional_args:
            assert isinstance(additional_args, dict), f"Parameter 'additional_args' must be dictionary but found type: {type(additional_args)} "
            payload.update(additional_args)

        res_api = self.wooApiObj.post('orders', data=payload, expected_status_code=201)
        return res_api

