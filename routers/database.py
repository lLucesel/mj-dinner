import MySQLdb
from MySQLdb.cursors import DictCursor


class MySQLClientConnector:
    def __init__(self, schema_nm, user_nm, password, host, port):
        self.conn = MySQLdb.connect(
            host=host,
            port=int(port),
            user=user_nm,
            password=password,
            db=schema_nm,
            charset='utf8mb4'
        )
        self.curs = self.conn.cursor(DictCursor)

    def executemany(self, query=None, args=None):
        return self.curs.executemany(query, args)

    def execute(self, query=None, args=None):
        return self.curs.execute(query, args)

    def fetchone(self, query=None, args=None):
        self.curs.execute(query, args)
        return self.curs.fetchone()

    def fetchall(self, query=None, args=None):
        self.curs.execute(query, args)
        return self.curs.fetchall()

    def commit(self):
        return self.conn.commit()

    def close(self):
        return self.conn.close()
