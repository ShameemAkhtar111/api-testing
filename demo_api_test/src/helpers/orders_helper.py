import json
import os


class OrdersHelper:

    def __init__(self):
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))

    def create_order(self, additional_args=None):
        payload_template = os.path.join(self.cur_file_dir, '..', 'data', 'create_order_payload.json')
        with open(payload_template) as file:
            payload = json.load(file)

        import pdb;pdb.set_trace()
