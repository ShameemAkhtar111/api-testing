import random
from demo_api_test.src.utilities.db_utilities import DbUtilities


class ProductsDAO:

    def __init__(self):
        self.db_helper = DbUtilities()

    def get_random_product_from_db(self, qty=1):

        sql = 'SELECT * FROM demosite.wp_posts WHERE post_type="product" LIMIT 5000;'
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql,int(qty))