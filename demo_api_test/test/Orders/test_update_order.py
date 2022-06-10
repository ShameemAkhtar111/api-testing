import pytest
from demo_api_test.src.helpers.orders_helper import OrdersHelper
from demo_api_test.src.utilities.wooComApiUtilities import WooComAPIUtilities
from demo_api_test.src.utilities.genericUtilities import generate_random_string

pytestmark = [pytest.mark.orders, pytest.mark.regression]


@pytest.mark.parametrize("new_status",
                         [
                             pytest.param("cancelled", marks=[pytest.mark.tcid55, pytest.mark.smoke]),
                             pytest.param("completed", marks=pytest.mark.tcid56),
                             pytest.param("on-hold", marks=pytest.mark.tcid57)
                         ])
def test_update_order_status(new_status):
    # create new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    # get current order status
    curr_status = order_json['status']
    assert curr_status != new_status, f"Current status of order is already {new_status}." \
                                      f"Unable to run test"

    # update order status
    order_id = order_json['id']
    payload = {"status": new_status}
    order_helper.update_order(order_id, payload)

    # get order info
    new_order_info = order_helper.retrieve_an_order(order_id)

    # verify new status order is what was updated
    assert new_order_info['status'] == new_status, f"Updated order status to {new_status}," \
                                                   f"but order status is still {new_order_info['status']}"


@pytest.mark.tcid58
def test_update_order_status_to_random_string():
    new_status = "sdgyuy"
    # create new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    order_id = order_json['id']

    # update order status
    payload = {"status": new_status}
    rs_api = WooComAPIUtilities().put(f'orders/{order_id}', params=payload, expected_status_code=400)
    assert rs_api['code'] == 'rest_invalid_param', f"Update order status to random string did not gave correct" \
                                                   f"code in response. Expected: 'rest_invalid_param', Actual:" \
                                                   f"{rs_api['code']}"

    assert rs_api['message'] == 'Invalid parameter(s): status', f"Update order status to random string did not" \
                                                                f" gave correctmessage in response." \
                                                                f" Expected: 'Invalid parameter(s): status'," \
                                                                f" Actual: {rs_api['message']}"


@pytest.mark.tcid59
def test_update_order_customer_note():
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    order_id = order_json['id']

    rand_str = generate_random_string(40)
    payload = {"customer_note": rand_str}
    order_helper.update_order(order_id, payload)

    new_order_info = order_helper.retrieve_an_order(order_id)
    assert new_order_info['customer_note'] == rand_str, f"Update order 'customer_note' failed." \
                                                        f"Expected: {rand_str}, Actual: {new_order_info['customer_note']}"
