import MySQLdb
from MySQLdb.cursors import DictCursor

if __name__ == '__main__':
    conn = MySQLdb.connect(
        host="mj.caletbhkxfd6.ap-northeast-2.rds.amazonaws.com",
        port=3306,
        user="admin_mj",
        password="77gundam77",
        db="dinner",
        charset='utf8mb4'
    )

    _cursor = conn.cursor(DictCursor)
#
    #q = """
#
    #INSERT INTO food (food_type_id, name, ingredient, spice, recipe, calorie, carbohydrate, protein, vitamin)
    #VALUES ('1','오이소박이','오이','고추가루','잘버무린다','3','3','3','3')"""
#
    #_cursor.execute(q)
    #conn.commit()

    q = """SELECT name, ingredient, spice, recipe, calorie, carbohydrate, protein, vitamin
    FROM food JOIN food_type ON food.food_type_id = food_type.id
    WHERE food_type_id = '1'
    """

    _cursor.execute(q)

    _rows = _cursor.fetchall()
    print(_rows)
