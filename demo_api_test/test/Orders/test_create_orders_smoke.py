import  pytest
from demo_api_test.src.dao.products_dao import ProductsDAO
from demo_api_test.src.helpers.orders_helper import OrdersHelper


@pytest.mark.tcid48
def test_create_paid_order_guest_user():
    product_dao = ProductsDAO()
    order_obj = OrdersHelper()

    # get a product from db
    rand_product = product_dao.get_random_product_from_db(1)
    product_id = rand_product[0]['ID']

    # make a call
    order_obj.create_order()

    # verify response

    # verify db