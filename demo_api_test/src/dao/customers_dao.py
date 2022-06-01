from demo_api_test.src.utilities.db_utilities import DbUtilities
import random


class CustomersDAO:

    def __init__(self):
        self.db_helper = DbUtilities()

    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM demosite.wp_users WHERE user_email = '{email}';"
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql

        # import pdb;pdb.set_trace()

    def get_random_customer_from_db(self, qty=1):
        sql = "SELECT * FROM demosite.wp_users ORDER BY id DESC LIMIT 5000;"
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql,int(qty))
