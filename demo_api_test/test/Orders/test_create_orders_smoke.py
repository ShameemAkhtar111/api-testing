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
    assert order_json, "Create order for guest user response is empty."
    assert order_json['customer_id'] == 0, f"Create order for guest user expected customer_id=0 but got {order_json['customer_id']}"
    assert len(order_json['line_items']) == 1, f"Expected only one item but found {len(order_json['line_items'])}" \
                                               f"for Order id: {order_json['id']}."
    # import pdb;pdb.set_trace()

    # verify response

    # verify db