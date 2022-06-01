import pymysql
import logging as logger
from demo_api_test.src.utilities.credentials_utility import CredentialsUtility


class DbUtilities:

    def __init__(self):
        self.creds = CredentialsUtility.get_db_credentials()
        self.host = '127.0.0.1'

    def create_connection(self):
        try:
            connection = pymysql.connect(host=self.host, user=self.creds['db_user'],
                                         password=self.creds['db_password'], port=8889)
        except Exception as e:
            raise Exception(f"Failed connecting to Database using {self.host}"
                            f"{self.creds['db_user']}, {self.creds['db_password']} getting exception as {str(e)}")
        return connection

    def execute_select(self, sql):
        con = self.create_connection()
        try:
            logger.debug(f"Executing sql: {sql}")
            cur = con.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            res_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running sql: {sql} \n Error: {str(e)} ")
        finally:
            con.close()

        return res_dict


    def execute_sql(self, sql):
        print("sql")
