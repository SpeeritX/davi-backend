import os
import pymysql


def mysqlconnect():
    conn = pymysql.connect(
        host=os.environ['HOST'],
        user=os.environ['USER'],
        password=os.environ['PASSWORD'],
        db='public',)

    cur = conn.cursor()
    return cur
