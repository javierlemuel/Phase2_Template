import pymysql
import pymysql.cursors


# Use this to access database
class Dbconnect:
    def __init__(self) -> None:
        self.connection = pymysql.connect(host='group2-db-ccom4115group2-2b06.a.aivencloud.com',
                                          db='defaultdb', port=12004, user='avnadmin', password='AVNS_UR3UBFJzMulx_RCqe5P')
        self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)

    def select(self, sql, params=None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)

        result = self.cursor.fetchall()
        return result

    def execute(self, sql, params=None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        self.connection.commit()
