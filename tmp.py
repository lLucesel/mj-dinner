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

_update = """
UPDATE food A
INNER JOIN food_type B ON A.food_type_id = B.id
SET A.ingredient = %s, A.spice = %s, A.recipe = %s,
A.calorie = %s, A.carbohydrate = %s, A.protein = %s, A.vitamin = %s
WHERE A.name = %s and food_type_id = 1
"""

name = '상추 겉절이'

values = ('상추에서 바꾸지 않아요', '고춧가루에서 바꾸지 않아요', '무치기에서 바꾸지 않아요',
          '333', '11', '22', '33')
print("!")
db.execute(_update, values)
print("!")
db.commit()
print("!")

