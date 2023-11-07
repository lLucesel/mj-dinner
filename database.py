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

    # food table에서 반찬(food_type_id = 1) 불러오기
    # side는 이름 관련 코드에서 씀. choice.py random, detail.py name
    def side(self):
        side = """
        SELECT *
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        WHERE food_type = '반찬'
        """
        self.curs.execute(side)
        return self.curs.fetchone()

    def soup(self):
        soup = """
        SELECT *
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        WHERE food_type = '국' 
        """
        self.curs.execute(soup)
        return self.curs.fetchone()

    def food_cal(self):
        _food_cal = """
        SELECT name, calorie
        FROM food JOIN food_type ON food.food_type_id = food_type.id
        """
        self.curs.execute(_food_cal)
        return self.curs.fetchall()
