import pytest
import pdb
from datetime import datetime, timedelta
from demo_api_test.src.helpers.products_helper import ProductsHelper



@pytest.mark.regression
class TestListProductsWithFilter:

    @pytest.mark.tcid51
    def test_list_products_with_filter_after(self):
        # create data
        x_days_from_today = 30
        _after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        after_created_date = _after_created_date.isoformat()

        # or you can generate your custom format by below code
        # temp_date = datetime.now() - timedelta(days=x_days_from_today)
        # after_created_date = temp_date.strftime('%Y-%m-%dT%H:%M:%S')

        payload = dict()
        payload['after'] = after_created_date


        # make api call
        rs_api = ProductsHelper().call_list_products(payload)
        assert rs_api, "Empty response for 'list products with filter'"
        pdb.set_trace()
        # get data from db

        # verify response