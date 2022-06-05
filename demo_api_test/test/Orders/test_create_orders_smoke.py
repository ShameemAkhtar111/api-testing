import pytest
from demo_api_test.src.dao.products_dao import ProductsDAO
from demo_api_test.src.dao.orders_dao import OrdersDao
from demo_api_test.src.helpers.orders_helper import OrdersHelper
from demo_api_test.src.utilities.wooComApiUtilities import WooComAPIUtilities

pytestmark = [pytest.mark.orders, pytest.mark.smoke]

@pytest.mark.tcid48
def test_create_paid_order_guest_user():
    product_dao = ProductsDAO()
    order_dao = OrdersDao()
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

    # verify response
    assert order_json, "Create order for guest user response is empty."
    assert order_json['customer_id'] == 0, f"Create order for guest user expected customer_id=0 but got {order_json['customer_id']}"
    assert len(order_json['line_items']) == 1, f"Expected only one item but found {len(order_json['line_items'])}" \
                                               f"for Order id: {order_json['id']}."
    # verify db

    line_info = order_dao.get_order_line_by_order_id(order_json['id'])
    assert line_info, f"Create orders, line item not found in DB. Order id: {order_json['id']}"
    line_items = [i for i in line_info if i['order_item_type'] == 'line_item']
    assert len(line_items) == 1, f"Expected 1 line item but got {len(line_items)}. Order id: {order_json['id']}"
    line_id = line_items[0]['order_item_id']
    line_details = order_dao.get_order_items_details(line_id)
    db_product_id = line_details['_product_id']

    assert str(db_product_id) == str(product_id), f"Create order, 'product id' in db does not matche in API." \
                                        f"API Product id: {product_id}, DB Product id: {product_id}"
