import pytest
from demo_api_test.src.dao.products_dao import ProductsDAO
from demo_api_test.src.dao.orders_dao import OrdersDao
from demo_api_test.src.helpers.orders_helper import OrdersHelper
from demo_api_test.src.helpers.customers_helper import CustomerHelper
from demo_api_test.src.utilities.wooComApiUtilities import WooComAPIUtilities


pytestmark = [pytest.mark.orders, pytest.mark.smoke]

@pytest.mark.tcid48
def test_create_paid_order_guest_user():
    product_dao = ProductsDAO()
    order_obj = OrdersHelper()

    # get a product from db
    rand_product = product_dao.get_random_product_from_db(1)
    product_id = rand_product[0]['ID']
    customer_id = 0
    info = {
        "line_items": [
            {
                "product_id": product_id,
                "quantity": 1
            }
        ],
        "customer_id": customer_id
    }

    # make a call
    order_json = order_obj.create_order(additional_args=info)

    # verify response
    expected_products = [{'product_id': product_id}]
    order_obj.verfiy_order_is_created(order_json, customer_id, expected_products)



@pytest.mark.tcid49
def test_create_paid_order_new_customer():
    product_dao = ProductsDAO()
    order_obj = OrdersHelper()
    customer_helper = CustomerHelper()

    rand_product = product_dao.get_random_product_from_db(1)
    product_id = rand_product[0]['ID']
    cust_info = customer_helper.create_customer()
    customer_id = cust_info['id']
    info = {
        "line_items": [
            {
                "product_id": product_id,
                "quantity": 1
            }
        ],
        "customer_id": customer_id
    }

    # make a call
    order_json = order_obj.create_order(additional_args=info)

    expected_products = [{'product_id': product_id}]
    order_obj.verfiy_order_is_created(order_json, customer_id, expected_products)
