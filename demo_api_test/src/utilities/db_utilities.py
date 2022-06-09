import os

import pymysql
import logging as logger
from demo_api_test.src.utilities.credentials_utility import CredentialsUtility
from demo_api_test.src.configs.host_config import DB_HOST


class DbUtilities:

    def __init__(self):
        self.creds = CredentialsUtility.get_db_credentials()

        self.machine = os.environ.get('MACHINE')
        assert self.machine, "Environment variable 'MACHINE' not found, please set 'MACHINE' in environment variables."

        self.wp_host = os.environ.get('WP_HOST')
        assert self.wp_host, "Environment variable 'WP_HOST' not found, please set 'WP_HOST' in environment variables."

        if self.machine == 'docker' and self.wp_host == 'local':
            raise Exception("can not run test in docker if 'WP_HOST'=local.")

        self.env = os.environ.get('ENV', 'test')

        self.host = DB_HOST[self.machine][self.env]['host']
        self.port = DB_HOST[self.machine][self.env]['port']
        self.database = DB_HOST[self.machine][self.env]['database']
        self.socket = DB_HOST[self.machine][self.env]['socket']
        self.table_prefix = DB_HOST[self.machine][self.env]['table_prefix']

    def create_connection(self):
        try:
            connection = pymysql.connect(host=self.host, user=self.creds['db_user'],
                                         password=self.creds['db_password'], port=self.port)
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
