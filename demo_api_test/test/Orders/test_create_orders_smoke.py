import pytest
from demo_api_test.src.dao.products_dao import ProductsDAO
from demo_api_test.src.dao.orders_dao import OrdersDao
from demo_api_test.src.helpers.orders_helper import OrdersHelper
from demo_api_test.src.helpers.customers_helper import CustomerHelper
from demo_api_test.src.utilities.wooComApiUtilities import WooComAPIUtilities

pytestmark = [pytest.mark.orders, pytest.mark.smoke]

@pytest.fixture(scope='module')
def orders_setup():
    product_dao = ProductsDAO()
    order_helper = OrdersHelper()
    rand_product = product_dao.get_random_product_from_db(1)
    product_id = rand_product[0]['ID']

    info = {'product_id': product_id,
            'order_helper': order_helper}

    return info


@pytest.mark.tcid48
def test_create_paid_order_guest_user(orders_setup):

    # get a product from db
    order_helper = orders_setup['order_helper']
    product_id = orders_setup['product_id']
    import pdb;pdb.set_trace()
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
    order_json = order_helper.create_order(additional_args=info)

    # verify response
    expected_products = [{'product_id': product_id}]
    order_helper.verfiy_order_is_created(order_json, customer_id, expected_products)



@pytest.mark.tcid49
def test_create_paid_order_new_customer(orders_setup):

    customer_helper = CustomerHelper()

    order_helper = orders_setup['order_helper']
    product_id = orders_setup['product_id']
    import pdb;pdb.set_trace()
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
    order_json = order_helper.create_order(additional_args=info)

    expected_products = [{'product_id': product_id}]
    order_helper.verfiy_order_is_created(order_json, customer_id, expected_products)
