import json
import os
from demo_api_test.src.utilities.wooComApiUtilities import WooComAPIUtilities
from demo_api_test.src.dao.orders_dao import OrdersDao


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

    def verfiy_order_is_created(self, order_json, exp_cust_id, exp_products):
        order_dao = OrdersDao()
        assert order_json, "Create order for guest user response is empty."
        assert order_json['customer_id'] == exp_cust_id, f"Create order for guest user expected customer_id: {exp_cust_id}" \
                                                  f" but got {order_json['customer_id']}"
        assert len(order_json['line_items']) == len(exp_products), f"Expected {len(exp_products)} item but found" \
                                                                   f" {len(order_json['line_items'])} for Order id: {order_json['id']}."
        # verify db

        line_info = order_dao.get_order_line_by_order_id(order_json['id'])
        assert line_info, f"Create orders, line item not found in DB. Order id: {order_json['id']}"
        line_items = [i for i in line_info if i['order_item_type'] == 'line_item']
        # assert len(line_items) == 1, f"Expected 1 line item but got {len(line_items)}. Order id: {order_json['id']}"

        api_product_ids = [i['product_id'] for i in order_json['line_items']]

        for product in exp_products:
            assert product['product_id'] in api_product_ids, f"Create order does not have at least one expected " \
                                                             f"product in DB. Product id: {product['product_id']}." \
                                                             f" Order id: {order_json['id']}. "
