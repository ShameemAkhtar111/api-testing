import os
from pprint import pprint
from demo_api_test.src.configs.host_config import WOO_API_HOST
from demo_api_test.src.utilities.credentials_utility import CredentialsUtility
from woocommerce import API
import logging as logger


class WooComAPIUtilities:

    def __init__(self):
        wc_creds = CredentialsUtility.get_wc_keys()
        self.env = os.environ.get("ENV", "test")
        self.base_url = WOO_API_HOST[self.env]
        self.wcapi = API(
            url=self.base_url,
            consumer_key=wc_creds['wc_key'],
            consumer_secret=wc_creds['wc_secret'],
            version="wc/v3",
            timeout = 10
        )

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad status code." \
                                                              f"Expected status code {self.expected_status_code} " \
                                                              f"but actual status code {self.status_code}, " \
                                                              f"Url: {self.url}, Response json: {self.rs_json}"

    def get(self, wc_endpoint, params=None, expected_status_code=200):
        self.url = self.base_url + "wp-json/wc/v3/" + wc_endpoint
        res = self.wcapi.get(wc_endpoint, params=params)
        self.status_code = res.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = res.json()
        self.assert_status_code()
        # import pdb; pdb.set_trace()
        logger.debug(f"GET API response: {self.rs_json}")
        return self.rs_json

    def post(self, wc_endpoint, data=None, expected_status_code=200):
        self.url = self.base_url + "wp-json/wc/v3/" + wc_endpoint
        res = self.wcapi.post(wc_endpoint, data=data)
        self.status_code = res.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = res.json()
        self.assert_status_code()
        logger.debug(f"POST API response: {self.rs_json}")
        return self.rs_json



if __name__ == '__main__':
    obj = WooComAPIUtilities()
    response_api = obj.get('products')
    pprint(response_api)
    # import pdb;pdb.set_trace()
