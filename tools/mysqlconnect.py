import os
import pymysql


def mysqlconnect():
    conn = pymysql.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        db='public',)

    cur = conn.cursor()
    return cur
