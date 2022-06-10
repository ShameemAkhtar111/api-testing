import pytest
import pdb
from datetime import datetime, timedelta
from demo_api_test.src.helpers.products_helper import ProductsHelper
from demo_api_test.src.dao.products_dao import ProductsDAO


@pytest.mark.regression
class TestListProductsWithFilter:

    @pytest.mark.tcid51
    def test_list_products_with_filter_after(self):
        # create data
        x_days_from_today = 1500
        _after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        after_created_date = _after_created_date.isoformat()

        # or you can generate your custom format by below code
        # temp_date = datetime.now() - timedelta(days=x_days_from_today)
        # after_created_date = temp_date.strftime('%Y-%m-%dT%H:%M:%S')

        payload = dict()
        payload['after'] = after_created_date
        # payload['per_page'] = 100

        # make api call
        rs_api = ProductsHelper().call_list_products(payload)
        assert rs_api, "Empty response for 'list products with filter'"

        # get data from db
        db_products = ProductsDAO().get_product_after_given_date(after_created_date)

        # verify response matches with db
        assert len(rs_api) == len(db_products), f"List of product with filter 'after' returned unexpected  number" \
                                                f"of products. Expected: {len(db_products)}, Actual: {len(rs_api)}"

        ids_in_rs_api = [i['id'] for i in rs_api]
        ids_in_db = [i['ID'] for i in db_products]

        ids_diff = list(set(ids_in_rs_api) - set(ids_in_db))

        assert not ids_diff, "List products with filter, product ids mismatch with db."
