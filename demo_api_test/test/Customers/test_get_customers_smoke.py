import pytest
from demo_api_test.src.utilities.request_utilities import RequestUtilities


@pytest.mark.customers
@pytest.mark.tcid30
def test_get_all_customers():
    req_obj = RequestUtilities()
    res_get = req_obj.get('customers')

    assert res_get, f"Response of list all customers is empty."

    # import pdb;pdb.set_trace()
