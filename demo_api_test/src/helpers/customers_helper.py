
from demo_api_test.src.utilities.genericUtilities import generate_random_email_and_password
from demo_api_test.src.utilities.request_utilities import RequestUtilities


class CustomerHelper:

    def __init__(self):
        self.request_obj = RequestUtilities()

    def create_customer(self, email=None, password=None, **kwargs):

        if not email:
            ep = generate_random_email_and_password()
            email = ep["email"]

        if not password:
            password = "Password1"

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)
        created_customer_json = self.request_obj.post('customers', payload=payload, expected_status_code=201)

        return created_customer_json
