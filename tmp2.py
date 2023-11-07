from choice import FoodChoice
from database import MySQLClientConnector
from diet import FoodDiet
from detail import FoodDetail
from models import Food, FoodType

db_name = "dinner"
user = "admin_mj"
password = "77gundam77"
host = "mj.caletbhkxfd6.ap-northeast-2.rds.amazonaws.com"
port = 3306

db = MySQLClientConnector(db_name, user, password, host, port)
_food_choice = FoodChoice(db_name, user, password, host, port)
_food_detail = FoodDetail(db_name, user, password, host, port)
_food_diet = FoodDiet(db_name, user, password, host, port)

_food = Food

new = """
    INSERT INTO food (food_type_id, name, ingredient, spice, recipe,
    calorie, carbohydrate, protein, vitamin)
    VALUES (%s, %s, %s, %s, %s,
    %s, %s, %s, %s)
    """
_new = ('1',
        '테스트메뉴1', '등갈비, 김치', '고춧가루', '넣고 끓인다.',
        '890', '6', '7', '8')
print("1")
db.execute(new, _new)
print('2')
db.commit()
print("#")

# 등록한 메뉴칸'만' 쓴다
# update인데? 왜지??
