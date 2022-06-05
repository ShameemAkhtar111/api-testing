from demo_api_test.src.utilities.db_utilities import DbUtilities


class OrdersDao:
    def __init__(self):
        self.db_utility = DbUtilities()

    def get_order_line_by_order_id(self,order_id):
        sql= f"SELECT * FROM demosite.wp_woocommerce_order_items WHERE order_id={order_id};"
        return self.db_utility.execute_select(sql)