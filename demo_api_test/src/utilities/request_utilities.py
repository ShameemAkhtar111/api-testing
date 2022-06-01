import requests
import os
import json
import logging as logger
from demo_api_test.src.configs.host_config import API_HOST
from demo_api_test.src.utilities.credentials_utility import CredentialsUtility
from requests_oauthlib import OAuth1


class RequestUtilities:

    def __init__(self):
        wc_creds = CredentialsUtility.get_wc_keys()
        self.env = os.environ.get("ENV", "test")
        self.base_url = API_HOST[self.env]
        self.auth = OAuth1(wc_creds['wc_key'], wc_creds['wc_secret'])

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad status code." \
                                                              f"Expected status code {self.expected_status_code} " \
                                                              f"but actual status code {self.status_code}, " \
                                                              f"Url: {self.url}, Response json: {self.rs_json}"

    def post(self, endpoint, payload=None, header=None, expected_status_code=200):
        if not header:
            header = {"content-type": "application/json"}
        self.url = self.base_url + endpoint
        res = requests.post(url=self.url, data=json.dumps(payload), headers=header, auth=self.auth)
        self.status_code = res.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = res.json()
        self.assert_status_code()
        # import pdb; pdb.set_trace()
        # print('post')
        logger.debug(f"POST API response: {self.rs_json}")
        return self.rs_json

    def get(self, endpoint, payload=None, header=None, expected_status_code=200 ):
        if not header:
            header = {"content-type": "application/json"}
        self.url = self.base_url + endpoint
        res = requests.get(url=self.url, data=json.dumps(payload), headers=header, auth=self.auth)
        self.status_code = res.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = res.json()
        self.assert_status_code()
        # import pdb; pdb.set_trace()
        logger.debug(f"GET API response: {self.rs_json}")
        return self.rs_json
