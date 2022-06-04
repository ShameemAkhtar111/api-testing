import pytest
from demo_api_test.src.dao.products_dao import ProductsDAO
from demo_api_test.src.helpers.orders_helper import OrdersHelper
from demo_api_test.src.utilities.wooComApiUtilities import WooComAPIUtilities


@pytest.mark.tcid48
def test_create_paid_order_guest_user():
    product_dao = ProductsDAO()
    order_obj = OrdersHelper()

    # get a product from db
    rand_product = product_dao.get_random_product_from_db(1)
    product_id = rand_product[0]['ID']
    info = {
        "line_items": [
            {
                "product_id": product_id,
                "quantity": 1
            }
        ]
    }

    # make a call
    order_json = order_obj.create_order(additional_args=info)
    import pdb;pdb.set_trace()

    # verify response

    # verify db