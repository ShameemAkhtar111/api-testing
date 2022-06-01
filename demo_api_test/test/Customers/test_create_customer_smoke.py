import pytest
import logging as logger
from demo_api_test.src.utilities.genericUtilities import generate_random_email_and_password
from demo_api_test.src.helpers.customers_helper import CustomerHelper
from demo_api_test.src.dao.customers_dao import CustomersDAO
from demo_api_test.src.utilities.request_utilities import RequestUtilities


@pytest.mark.customers
@pytest.mark.tcid29
def test_create_customer_only_email_password():
    logger.info("TEST: Create new customer with email and password only.")
    random_info = generate_random_email_and_password()
    email = random_info['email']
    password = random_info['password']

    custobj = CustomerHelper()
    cust_api_info = custobj.create_customer(email=email)
    assert cust_api_info['email'] == email,\
        f"Create customer api returns wrong email. Email:{email}, Response Email:{cust_api_info['email']}"

    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)

    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID']

    assert id_in_api == id_in_db , f"Create customer response 'id' is not equal to 'ID' in database." \
                                   f"Email: {email}"


@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():
    cust_dao = CustomersDAO()
    existing_cust = cust_dao.get_random_customer_from_db()
    existing_email = existing_cust[0]['user_email']
    req_helper = RequestUtilities()
    payload = {"email":existing_email, "password":"Passowrd1"}
    cust_api_info = req_helper.post(endpoint='customers', payload=payload,expected_status_code=400)
    assert cust_api_info['code'] == 'registration-error-email-exists', f"Create customer with existing user" \
                                                                       f"error 'code' is not correct. " \
                                                                       f"Expected: 'registration-error-email-exists', "\
                                                                       f"Actual: {cust_api_info['code']}"
    # import pdb;pdb.set_trace()