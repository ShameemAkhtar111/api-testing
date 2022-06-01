import pytest
from demo_api_test.src.utilities.request_utilities import RequestUtilities
from demo_api_test.src.dao.products_dao import ProductsDAO
from demo_api_test.src.helpers.products_helper import ProductsHelper


pytestmark = [pytest.mark.products, pytest.mark.smoke]


@pytest.mark.tcid24
def test_get_all_products():
    req_obj = RequestUtilities()
    res_get = req_obj.get('products')

    assert res_get, f"Response of list all products is empty."


@pytest.mark.tcid25
def test_get_product_by_id():
    # get productid from db
    rand_product = ProductsDAO().get_random_product_from_db(1)
    rand_product_id = rand_product[0]['ID']
    db_product_name = rand_product[0]['post_title']

    # call the api
    products_helper = ProductsHelper()
    rs_api = products_helper.get_product_by_id(rand_product_id)
    api_product_name = rs_api['name']

    # verify the response
    assert db_product_name == api_product_name, f"Get product by id returned wrong product. Id:{rand_product_id}" \
                                                f"Db name: {db_product_name}, Api name: {api_product_name}"
    # import pdb;pdb.set_trace()
