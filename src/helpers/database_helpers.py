import pymysql
from pymysql.cursors import DictCursor
from src.helpers.config_helpers import get_database_credentials
from src.configs.generic_configs import GenericConfigs


def read_from_db(sql_query):
    db_creds = get_database_credentials()
    # connect to db
    # read from db
    connection = pymysql.connect(host=db_creds['db_host'], port=db_creds['db_port'],
                                 user=db_creds['db_user'], password=db_creds['db_password'])
    try:
        cursor = connection.cursor(DictCursor)
        cursor.execute(sql_query)
        db_data = cursor.fetchall()
        cursor.close()
    finally:
        connection.close()
    # return the result

    return db_data


def get_order_from_db_by_order_no(order_no):
    table_prefix = GenericConfigs.DB_TABLE_PREFIX
    schema = GenericConfigs.DATABASE_SCHEMA
    sql = f"SELECT * FROM {schema}.{table_prefix}posts " \
          f"WHERE post_type = 'shop_order' AND ID = {order_no};"

    # quicksitedb.wp_posts

    db_order = read_from_db(sql)
    # import pdb; pdb.set_trace()
    # print(db_order)
    return db_order


